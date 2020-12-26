# https://xgboost.readthedocs.io/en/latest/tutorials/model.html
# https://www.kaggle.com/robikscube/tutorial-time-series-forecasting-with-xgboost

# conda  search xgboost
# conda install py-xgboost-cpu

import time
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import xgboost as xgb
from xgboost import plot_importance, plot_tree
from sklearn.metrics import mean_squared_error, mean_absolute_error

import datastore

def query(sql):
  datastore.start_transaction(readonly=True)
  d=datastore.query(sql)
  datastore.commit()
  return d


def company_daily(company, start, end, granularity=None):
  if granularity == 'hour':
         timescale= '%%Y-%%m-%%d %%H'
  else: # day
         timescale= '%%Y-%%m-%%d'

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   SUM(bytes) * 1.0 / (1024.0 * 1024.0) as MB 
   FROM jangle_traffic_total
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company =  {company}
   GROUP BY date
   ORDER BY date
  """

  return SQL

def mean_absolute_percentage_error(y_true, y_pred):
    """Calculates MAPE given y_true and y_pred"""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def create_features(df, label=None):
    """
    Creates time series features from datetime index
    """
    df['ddate'] =  df.index
    print(df['ddate'])
    df['hour'] = df['ddate'].dt.hour
    df['dayofweek'] = df['ddate'].dt.dayofweek
    #df['quarter'] = df['date'].dt.quarter
    df['month'] = df['ddate'].dt.month
    df['year'] = df['ddate'].dt.year
    #df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['ddate'].dt.day
    #df['weekofyear'] = df['date'].dt.weekofyear

    X = df[[
            'hour',
            'dayofweek',
          #  'quarter',
            'month',
            'year',
          #  'dayofyear',
            'dayofmonth'
          #  'weekofyear'
          ]]
    if label:
        y = df[label]
        return X, y
    return X

if __name__ == "__main__" :
  datastore.connect()
  # COMPANY_LIST=(3666, 3659,3116)
  COMPANY_LIST=(3666,)
  start='2020-10-01'
  end  ='2020-12-31'
  for company in COMPANY_LIST:
     scale='hour'
     sql=company_daily(company, start, end, scale)
     print(sql)
     df=query(sql)
     print(df)

     print ("Apply index")
     df['date']=  pd.to_datetime(df['date'], format='%Y-%m-%d %H')
     #df=df.set_index('Datetime', inplace=True)
     #df=df.set_index('Datetime')
     print(df)
     print(df.info())

     print ("SET index")

     df.set_index('date', inplace=True)
     print(df)
     print(df.info())

     print (" Histogram ")
     df.plot.hist(bins=80, alpha=0.8, title='Hourly traffic size distribution (MB): bins=80', xlabel='MB hourly', figsize=(25, 5) )
     plt.show()

     print (" Time plot ")
     df.plot(style='.',   y='MB', linestyle='-', marker='o', title="Whole set"  , figsize=(25, 5))
     plt.show()

     print("len=", len(df))
     train_len=int(0.8*len(df))
     train=df[0:train_len].copy()

     test=df[train_len:].copy()
     test_len=len(test)

     #train.plot(style='.',   y='MB',   title="Train set")
     #plt.show()

     #test.plot(style='.',   y='MB', title="Test set")
     #plt.show()


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
              #'dayofmonth', 
              'hour',
             x_vars=[
                     'hour',
                     'dayofmonth',
                     'dayofweek',
                     #'month'
                     #'year',
                     # 'weekofyear'
                     ],
             y_vars='MB',
             height=5 
             #plot_kws={'alpha':0.15, 'linewidth':0}
            )
     plt.suptitle('Traffic by Day of Month, Day of Week and Hour')
     plt.show()

     #reg = xgb.XGBRegressor(n_estimators=1000)
     reg = xgb.XGBRegressor(n_estimators = 1600 , random_state = 0 , max_depth = 15)
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
    
     #ffrom=test.index[0] #  '2020-12-10'
     header="Train and prediction " + str(test.index[0]) + " -  " + str(test.index[-1])
     #to  ='2020-12-31'
     #predicted = all[ffrom:to]
     #print("Len predicted=", len(predicted))
     #print( predicted )
     #predicted[['MB','Prediction']].plot(title='Train and prediction', linestyle='-', marker='o', figsize=(25, 5))
     #plt.show()

     predicted_2 = all.loc[test.index[0]:test.index[-1]]
     print("Len predicted_2=", len(predicted_2))
     print( predicted_2 )
     predicted_2[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
     plt.show()

     mean_squared_error(
                     y_true=test['MB'],
                     y_pred=test['Prediction']
                   )

     mean_absolute_error(
                     y_true=test['MB'],
                     y_pred=test['Prediction']
                   )

     mean_absolute_percentage_error(y_true=test['MB'],
                   y_pred=test['Prediction'])



     test['error']     = test['MB'] - test['Prediction']
     test['abs_error'] = test['error'].apply(np.abs)
     error_by_day = test.groupby(['year','month','dayofmonth']) \
          .mean()[['MB','Prediction','error','abs_error']]

     print("Over forecasted days")
     print( error_by_day.sort_values('error', ascending=True).head(10))

     print("Worst absolute predicted days")
     print(error_by_day.sort_values('abs_error', ascending=False).head(10))

     print("Best predicted days")
     print(error_by_day.sort_values('abs_error', ascending=True).head(10))