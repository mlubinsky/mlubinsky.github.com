# https://www.kaggle.com/robikscube/tutorial-time-series-forecasting-with-xgboost
import time
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import datastore

import seaborn as sns
import matplotlib.pyplot as plt
import xgboost as xgb
from xgboost import plot_importance, plot_tree
from sklearn.metrics import mean_squared_error, mean_absolute_error

def query(sql):
  datastore.start_transaction(readonly=True)
  d=datastore.query(sql)
  datastore.commit()
  return d


def company_daily(company, start, end):
  timescale= '%%Y-%%m-%%d'

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   SUM(bytes) * 1.0 / (1024.0 * 1024.0) as MB 
   FROM jangle_traffic_total
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company = '{company}'
   GROUP BY date
   ORDER BY date
  """

  return SQL

def create_features(df, label=None):
    """
    Creates time series features from datetime index
    """
    df['ddate'] =  df.index
    print(df['ddate'])
    #df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['ddate'].dt.dayofweek
    #df['quarter'] = df['date'].dt.quarter
    df['month'] = df['ddate'].dt.month
    #df['year'] = df['date'].dt.year
    #df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['ddate'].dt.day
    #df['weekofyear'] = df['date'].dt.weekofyear

    X = df[[
          #  'hour',
            'dayofweek',
          #  'quarter',
            'month',
          #  'year',
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
  COMPANY_LIST=(3666, 3659,3116)
  COMPANY_LIST=(3666,)  
  start='2020-10-01'
  end  ='2020-12-31'
  for company in COMPANY_LIST:
     sql=company_daily(company, start, end)
     print(sql) 
     df=query(sql)
     print(df)


     
     print ("Apply index")
     df['date']=  pd.to_datetime(df['date'], format='%Y-%m-%d')
     #df=df.set_index('Datetime', inplace=True)
     #df=df.set_index('Datetime')
     print(df)
     print(df.info())
     
     print ("SET index")
     
     df.set_index('date', inplace=True)
     print(df)
     print(df.info())
     
     print ("===========")

     df.plot(style='.',   y='MB')
     plt.show()

     split_date = '2020-12-01'
     train = df.loc[df.index <  split_date].copy()
     test =  df.loc[df.index >= split_date].copy()

     train.plot(style='.',   y='MB')
     plt.show()

     test.plot(style='.',   y='MB')
     plt.show()

     concat= test.rename(columns={'MB':'TEST'}) \
     .join( train.rename(columns={'MB':'TRAIN'}) , how='outer')

     concat.plot(title='concat', style='.')
     plt.show()


     X_train, y_train = create_features(train, label='MB')
     X_test,  y_test  = create_features(test,  label='MB')

     reg = xgb.XGBRegressor(n_estimators=1000)
     reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        early_stopping_rounds=50,
        verbose=False)
     plot_importance(reg, height=0.9)
     plt.show()

     test['Prediction'] = reg.predict(X_test)
     all = pd.concat([test, train], sort=False)
     all[['MB','Prediction']].plot(figsize=(15, 5))
     plt.show()







