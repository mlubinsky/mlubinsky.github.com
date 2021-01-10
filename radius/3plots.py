import time
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import xgboost as xgb  # conda install py-xgboost-cpu
from xgboost import plot_importance, plot_tree
import datastore

#--------------
def query(sql):
#-------------
  datastore.start_transaction(readonly=True)
  d=datastore.query(sql)
  datastore.commit()
  return d

#----------------------------------
def company_jangle_traffic_per_device(company, start, end, direction=None): # granularity='hour'):
#-----------------------------------  
  #if granularity == 'hour':
  timescale= '%%Y-%%m-%%d %%H'
  #else: # day
  #       timescale= '%%Y-%%m-%%d'

  #print(timescale)
  if not direction:
    filter="1=1"
  else:
    filter="direction="+str(direction) 

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   (SUM(bytes) * 1.0 / (1024.0 * 1024.0)  / count(distinct msisdn)) as MB,
   count(distinct msisdn) as n_msisdn
   FROM jangle_traffic
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company =  {company}
   and {filter}
   GROUP BY date
   ORDER BY date
  """

  return SQL


#-----------------------------------
def create_features(df, label=None):
#-----------------------------------
#  https://pandas-docs.github.io/pandas-docs-travis/reference/api/pandas.DatetimeIndex.html
    df['hour'] = df.index.hour
    df["morning"] = ((df['hour'] >= 7) & (df['hour'] <= 11)).astype('int')
    df["middleday"] = ((df['hour'] >= 12) & (df['hour'] <= 18)).astype('int')
    df["evening"] = ((df['hour'] >= 19) & (df['hour'] <= 23)).astype('int')
    df["night"] = ((df['hour'] >= 0) & (df['hour'] <= 6)).astype('int')

    df['dayofweek'] = df.index.dayofweek

    first_date=df.index.array[0]
    print(first_date)
    #exit(0)

    df['daysfromstart'] = 1 + (df.index - first_date).astype('timedelta64[D]').astype(int)

    print(df['daysfromstart'])

    X = df[[
            'hour',
            'dayofweek',
            'daysfromstart',
            'morning',
            'middleday',
            'evening',
            'night'
          ]]
    if label:
        y = df[label]
        return X, y


    return X

#----------------
def predict_xgboost(df, comment):
#-----------------
     df=df.drop('n_msisdn', axis=1)
     split=0.8
     train_len=int( split * len(df) ) 
     train=df[0:train_len].copy()

     test=df[train_len:].copy()
     test_len=len(test)
     print("train_len=", train_len, "test_len=", test_len)


     print(test)

     print(test.info())
     print(test.describe())
     print(test.columns )
     #exit(0)

     concat= test.rename(columns={'MB':'TEST'}) \
     .join( train.rename(columns={'MB':'TRAIN'}) , how='outer')

     concat.plot(title='Train: '+str(train_len) + ' points and Test: '+str(test_len) + " points", linestyle='-', marker='o', figsize=(25, 5))
     plt.show()


     X_train, y_train = create_features(train, label='MB')
     X_test,  y_test  = create_features(test,  label='MB')

     # https://www.kaggle.com/robikscube/time-series-forecasting-with-prophet
     features_and_target = pd.concat([X_train, y_train], axis=1)
     print(features_and_target.head())
     sns.pairplot(features_and_target.dropna(),
             hue=
              'hour',
             x_vars=[
              'hour',
              'dayofweek',
              'daysfromstart',
              'morning',
              'middleday',
              'evening',
              'night'
             ],
             y_vars='MB',
             height=5 
             #plot_kws={'alpha':0.15, 'linewidth':0}
            )
     plt.suptitle('Traffic by Day of Month, Day of Week and Hour')
     plt.show()

     #reg = xgb.XGBRegressor(n_estimators=1000)
     reg = xgb.XGBRegressor(
       n_estimators = 1600 , 
       random_state = 0 , 
       max_depth = 15)

     #reg = XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
     #    colsample_bynode=1, colsample_bytree=0.3, gamma=0,
     #    importance_type='gain', learning_rate=0.1, max_delta_step=0,
     #    max_depth=15, min_child_weight=1, missing=None, n_estimators=1000,
     #   n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
     #    reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
     #    silent=None, subsample=0.5, verbosity=1) 


     reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        early_stopping_rounds=50,
        verbose=False)
     plot_importance(reg, height=0.9)
     plt.show()

     test['Prediction'] = reg.predict(X_test)
     all = pd.concat([test, train], sort=False)
     all[['MB','Prediction']].plot(title='Train and prediction', linestyle='-', marker='o', figsize=(25, 5))
     plt.show()

     print ("Len all=", len(all))
     print (  "Train len=",   len(train), train.index[0], train.index[-1])
     print (  "Test  len=",   len(test),  test.index[0],  test.index[-1])

     header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])

     predicted   = all.loc[test.index[0]:test.index[-1]]
     print("Len predicted =", len(predicted ))
     print( predicted )
     predicted[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
     plt.show() 

def get_company():
   company_input=input("Company: (default 3659) :")
   if not company_input:
        return 3659
   else:
       return int(company_input)
#----------------
def get_start():
#---------------
  start_input = input("Enter start day (YYYY-MM-DD) (default 2020-11-01) : ")
  if not start_input:
      return "2020-11-01"
  elif  len(start_input) != 10:
      print("Error in input- format is YYYY-MM-DD")
      exit(1)
  else:
      return start_input

#------------------
def get_duration():
#-----------------
      duration = input("""Enter duration in days (default 7 days) :  """)

      if not duration :
         return 7  # 1 week
      else:
         return int(duration)
#------------
def main():
#----------

  datastore.connect()

  width=15
  height=5
  plt.rcParams['figure.figsize'] = [width, height]

  #COMPANY_LIST=(3659,3116, 3666)
  #COMPANY_LIST=(3666,)
  #start='2020-10-01'
  #end  ='2021-01-01'
  company=get_company()
  COMPANY_LIST=[]
  COMPANY_LIST.append(company)
  start = get_start()
  n_days=get_duration()
  end = (datetime.strptime(start, '%Y-%m-%d') + timedelta(days=n_days)).strftime('%Y-%m-%d')

  for company in COMPANY_LIST:
    for direction in [1,2]:
     print(company, direction)



     sql = company_jangle_traffic_per_device(company, start, end, direction)
     print(sql)
     df=query(sql)
     print(df)
     print(df.describe())
#     df.plot(title="no indexed")
#     plt.show()

     # index
     range  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
     #df = df.set_index('date').reindex(r).fillna(1.0).rename_axis('date').reset_index()
     df['date'] = pd.to_datetime(df['date'])
     df.set_index('date', inplace=True)
     df=df.reindex(range)
     print(df.index)
     print(df.count())
     print( "df[MB].count()=")
     print(df["MB"].count())

     print("fill NA with 0")
     df=df.fillna(0)
     #df.index.freq='H'

     print(df.count())
     print( "df[MB].count()=")
     print(df["MB"].count()) 

     print(df.describe())

 
     head="Company=" + str(company) + ". Traffic per device " + start + ' - ' + end + "  direction="+str(direction)
     df.plot(title=head)
     plt.show()

     df.plot(title=head, style=".")
     plt.show()
     
    
     #df.plot(title=head, ylim=(0,200))
     #plt.show()

     comment="XGBoost. Traffic per # of devices. Company "+ str(company) 
     predict_xgboost(df, comment) 

if __name__ == "__main__":
   main()
