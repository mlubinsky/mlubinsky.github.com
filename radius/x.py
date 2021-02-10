import time
from datetime import datetime, timedelta
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV, cross_validate, ParameterGrid

# from sklearn.cross_validate import StratifiedKFold, KFold
# from sklearn.grid_search import ParameterGrid
from sklearn.metrics import mean_squared_error

import xgboost as xgb
from xgboost import plot_importance, plot_tree

# https://www.mikulskibartosz.name/xgboost-hyperparameter-tuning-in-python-using-grid-search/
# https://machinelearningmastery.com/auto-sklearn-for-automated-machine-learning-in-python/
#
PI=math.pi
print("PI", PI)

#-----------------------------------
def create_features(df, label, first_date, useLags=False):
#-----------------------------------
#  https://pandas-docs.github.io/pandas-docs-travis/reference/api/pandas.DatetimeIndex.html
    df['hour'] = df.index.hour
    df["morning"] = ((df['hour'] >= 7) & (df['hour'] <= 11)).astype('int')
    df["middleday"] = ((df['hour'] >= 12) & (df['hour'] <= 18)).astype('int')
    df["evening"] = ((df['hour'] >= 19) & (df['hour'] <= 23)).astype('int')
    df["night"] = ((df['hour'] >= 0) & (df['hour'] <= 6)).astype('int')
    df['dayofweek'] = df.index.dayofweek
    #first_date=df.index.array[0]
    #print(first_date)
    #exit(0)

    df['daysfromstart'] = 1 + (df.index - first_date).astype('timedelta64[D]').astype(int)
    df['hours_from_start'] =  (df.index - first_date).astype('timedelta64[h]').astype(int)

    #print(df['daysfromstart'])
    print("Adding lag")
    if useLags:
      df["Lag_1"]=df["y"].shift(1)
      df["Lag_2"]=df["y"].shift(2)
      df["Lag_3"]=df["y"].shift(3)
      df["Lag_4"]=df["y"].shift(4)

      X = df[[
            'hour',
            'dayofweek',
            'daysfromstart',
            'hours_from_start',
            'morning',
            'middleday',
            'evening',
            'night',
            'Lag_1',
            'Lag_2',
            'Lag_3',
            'Lag_4'
          ]]
    else: # not use Lags
      X = df[[
            'hour',
            'dayofweek',
            'daysfromstart',
            'hours_from_start',
            'morning',
            'middleday',
            'evening',
            'night'
      ]]

    y=df[label]
    return X, y

#-------------------
def y_sin(df, amplitude, period=1, const=5 ):
  df['y'] = const + amplitude * ( np.sin(df.index.hour * period * PI  /24.0 ) - 0.2 * np.cos(df.index.hour * period * PI  /24.0 ) )

def  y_linear(df, k, a=0.0):
   first_timepoint=df.index.array[0]
   #df['daysfromstart'] = 1 + (df.index - first_timepoint).astype('timedelta64[D]').astype(int)
   hours_from_start =  (df.index - first_timepoint).astype('timedelta64[h]').astype(int)
   #df["hours_from_start"] = hours_from_start
   df['y'] = a + k * hours_from_start

def y_sin_and_linear(df, sin_amplitude, sin_period, k_linear, a_linear):
    first_timepoint=df.index.array[0]
    hours_from_start =  (df.index - first_timepoint).astype('timedelta64[h]').astype(int)
    df['y'] = a_linear + k_linear * hours_from_start + sin_amplitude * np.sin(df.index.hour * sin_period * PI  /24.0 )

def f():
   return 11


def find_hyperparams(X_train, y_train,  X_test, y_test):

 param_grid = [
              {'silent': [1],
               'nthread': [2],
               'eval_metric': ['rmse'],
               'eta': [0.03],
               'objective': ['reg:linear'],
               'max_depth': [5, 7],
               'num_round': [1000],
               'subsample': [0.2, 0.4, 0.6],
               'colsample_bytree': [0.3, 0.5, 0.7],
               }
              ]

# https://medium.com/datadriveninvestor/an-introduction-to-grid-search-ff57adcc0998
# Hyperparmeter grid optimization
 for params in ParameterGrid(param_grid):
    print(params)
    # Determine best n_rounds
    xgboost_rounds = []
    for train_index, test_index in kfold:
        X_train, X_test = train[train_index], train[test_index]
        y_train, y_test = target[train_index], target[test_index]

        xg_train = xgb.DMatrix(X_train, label=y_train)
        xg_test = xgb.DMatrix(X_test, label=y_test)

        watchlist = [(xg_train, 'train'), (xg_test, 'test')]

        num_round = params['num_round']
        xgclassifier = xgb.train(params, xg_train, num_round,
                                     watchlist,
                                     early_stopping_rounds=early_stopping);
        xgboost_rounds.append(xgclassifier.best_iteration)

    num_round = int(np.mean(xgboost_rounds))
    print('The best n_rounds is %d' % num_round)
    # Solve CV
    rmsle_score = []
    for cv_train_index, cv_test_index in kfold:
        X_train, X_test = train[cv_train_index, :], train[cv_test_index, :]
        y_train, y_test = target[cv_train_index], target[cv_test_index]

        # train machine learning
        xg_train = xgb.DMatrix(X_train, label=y_train)
        xg_test  = xgb.DMatrix(X_test, label=y_test)

        watchlist = [(xg_train, 'train'), (xg_test, 'test')]

        xgclassifier = xgb.train(params, xg_train, num_round);

        # predict
        predicted_results = xgclassifier.predict(xg_test)
        rmsle_score.append(np.sqrt(mean_squared_error(y_test, predicted_results)))

    if SCORE_MIN:
        if best_score > np.mean(rmsle_score):
            print(np.mean(rmsle_score))
            print('new best')
            best_score = np.mean(rmsle_score)
            best_params = params
            best_iter = num_round
    else:
        if best_score < np.mean(rmsle_score):
            print(np.mean(rmsle_score))
            print('new best')
            best_score = np.mean(rmsle_score)
            best_params = params
            best_iter = num_round


# Solution using best parameters
 print('best params: %s' % best_params)
 print('best score: %f' % best_score)
 xg_train = xgb.DMatrix(train, label=target)
 xg_test = xgb.DMatrix(test)
 watchlist = [(xg_train, 'train')]
 num_round = int(best_iter * test_round_fac)  # There are more samples so I can use more lines
 xgclassifier = xgb.train(best_params, xg_train, num_round, watchlist)
 return 1

#------------------
def predict_xgboost(df, comment, useLags, split=0.9, show_details=True):
#-----------------

     if useLags:
        train_len = len(df)-1
     else:
        #split=0.8  # between test and train
        train_len=int( split * len(df) )


     train=df[0:train_len].copy()
     test=df[train_len:].copy()
     test_len=len(test)

#  https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
#  https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/
#  https://towardsdatascience.com/doing-xgboost-hyper-parameter-tuning-the-smart-way-part-1-of-2-f6d255a45dde
#  https://towardsdatascience.com/selecting-optimal-parameters-for-xgboost-model-training-c7cd9ed5e45e
#  https://blog.cambridgespark.com/hyperparameter-tuning-in-xgboost-4ff9100a3b2f
     mean_train = np.mean(train["y"])
     print("mean train=", mean_train)

# Get predictions on the test set
     # baseline_predictions =  mean_train
     baseline_predictions = np.ones(test["y"].shape) * mean_train
# Compute MAE
     mae_baseline = mean_absolute_error(test["y"], baseline_predictions)
     print("Baseline MAE is {:.2f}".format(mae_baseline))

     # exit(0)

     a = test.rename(columns={'y':'TEST'})
     b = train.rename(columns={'y':'TRAIN'})


     concat = pd.merge(a, b, right_index=True, left_index=True, how='outer')
     # concat = a.join(b, how='outer')
     print(concat)

     concat.drop('Date_x', axis=1, inplace=True)
     concat.drop('Date_y', axis=1, inplace=True)

     print(concat)
   
#     concat = test.rename(columns={'y':'TEST'}) \
#     .join( train.rename(columns={'y':'TRAIN'}) , how='outer')


     header=comment + ' Train: '+str(train_len) + ' points and Test: '+str(test_len) + " points"
     if show_details:
       concat.plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

     first_date=train.index.array[0]
     X_train, y_train = create_features(train, 'y', first_date, useLags)
     print("len(X_train)=", len(X_train), "len(Y_train)=",len(y_train))

     X_test,  y_test  = create_features(test,  'y', first_date, useLags)
     print("len(X_test)=", len(X_test), "len(Y_test)=",len(y_test))

     #print( X_test.info() )
     #X_test.plot(y="hours_from_start", title="X_test hours from start")
     #plt.show()

     #print( X_train.info() )
     #X_train.plot(y="hours_from_start", title="X_train hours from start")
     #plt.show()

     #find_hyperparams( X_train, y_train, X_test,  y_test )
     #return
     # https://www.kaggle.com/robikscube/time-series-forecasting-with-prophet
     #features_and_target = pd.concat([X_train, y_train], axis=1)
     #print(features_and_target.head())


     #x_vars=[
     #         'hour',
     #         'dayofweek',
     #         'daysfromstart',
     #         'morning',
     #         'middleday',
     #         'evening',
     #         'night'
     #        ]
     #if useLags:
     #        x_vars.append('Lag_1')
     #        x_vars.append('Lag_2')
     #        x_vars.append('Lag_3')
     #        x_vars.append('Lag_4')


     model = xgb.XGBRegressor(
       n_estimators = 1600 ,
       random_state = 10 ,
       objective='reg:squarederror',  
       #objective= 'reg:linear',
       #objective='binary:logistic',
       learning_rate = 0.1,
       min_child_weight=1,
       gamma=0, 
       subsample=0.8, 
       colsample_bytree=0.8,
       # booster:'gblinear',
       booster= 'gbtree',
       max_depth = 35)

     # model = XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
     #    colsample_bynode=1, colsample_bytree=0.3, gamma=0,
     #    importance_type='gain', learning_rate=0.1, max_delta_step=0,
     #    max_depth=15, min_child_weight=1, missing=None, n_estimators=1000,
     #   n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
     #    reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
     #    silent=None, subsample=0.5, verbosity=1) 


     model.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        early_stopping_rounds=500,
        verbose=False)

     # Feature importance
     if show_details:
       plot_importance(model, height=0.9)
       plt.show()

     print("Before Prediction")
     test['Prediction'] = model.predict(X_test)


     print("Before concat len(test)=",len(test), "  len(train)=",len(train))
     all = pd.concat([test, train], sort=False)
     print("After concat len(all)=",len(all))

     if not useLags:
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       all[['y','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

     print ("Len all=", len(all))
     print (  "Train len=",   len(train), train.index[0], train.index[-1])
     print (  "Test  len=",   len(test),  test.index[0],  test.index[-1])

     predicted   = all.loc[test.index[0]:test.index[-1]]
     print("Len predicted =", len(predicted ))
     print( "predicted=" )
     print( predicted )

     if not useLags:
        predicted[['y','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
        plt.show()
        return

     print("test.dtypes=")
     print(test.dtypes)
     print("df.dtypes=")
     print(df.dtypes)

     print("test=")
     print(test)
     cols=['y','hour', 'morning', 'middleday', 'evening', 'night', 'dayofweek','daysfromstart', 'hours_from_start', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4']
     test.drop(columns=cols, inplace=True)

     test.rename(columns = {'Prediction':'y'}, inplace = True) 
     print("after drop test=")
     print(test)

     cc = pd.concat([df[:-1], test], sort=True)
     #print ("len(c)=", len(cc))
     #print(cc.dtypes)
     print("Check the sort order below after concat")
     print(cc.tail(10))
     print("Check the sort order above ")

     #cols=['Date_x', 'Date_y', 'hours_from_start_x', 'hours_from_start_y']
     #cc.drop(columns=cols, inplace=True)
     #exit(0)
     #cols=['hour', 'morning', 'middleday', 'evening', 'night', 'dayofweek','daysfromstart', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4']
     #cols=['hour', 'morning', 'middleday', 'evening', 'night', 'dayofweek','daysfromstart', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4', 'Prediction']
     #cc.drop(columns=cols, inplace=True)
     return cc

def init_df(start_day, number_of_days):
   number_of_hours=number_of_days * 24
   rng = pd.date_range(start_day, periods=number_of_hours, freq='H')
   df = pd.DataFrame({ 'Date': rng, 'y': 1 }, index=rng)
   return df

def use_lagged():
       N_points=5

       n_days=10
       df = init_df('2015-02-24', n_days)
       y_sin(df, amplitude=0.5, period=1, const=100)

       head=df[:-N_points].copy()
       tail=df[-N_points:].copy()
       useLags=True
       comment = "Use lagged values"
         #head=df.copy()
       all = predict_xgboost(head, comment, useLags)
       print (all.tail())
       print("i=0 after predict_xgboost len=",len(all))

       for i in range(0, N_points):
           print("---i=", i)
           print("-- step 1: tail.index[i]=")
           print(tail.index[i])
           print("one_rec=") 
           one_rec = tail[tail.index == tail.index[i]]
           print(one_rec)

           print("-- step 4a - BEFORE concatenate: all.tail(10)=")
           print (all.tail(10))
           all=pd.concat([all, one_rec], sort=True)
           print("-- step 4 - after concatenate: all.tail(10)=")
           print (all.tail(10))
           print("Make sure the order of time above is correct!!! ")
           #exit(0)
           all = predict_xgboost(all, comment, useLags)
           print("i=", i," after predict_xgboost len=",len(all))

       # Final plot
       pred = all[-i:].copy()
       pred.rename (columns={'y':'Prediction'}, inplace=True)
       #  Plot
       x = pd.concat([df, pred], axis=1, join="outer")
       print("After concat join=outer len(x)=",len(x))
       print(x)
       print(x.index)
       print("x.tail(10)=")
       print(x.tail(10))
       print(" is sort good above join=outer")
       # https://realpython.com/pandas-merge-join-and-concat/
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       header=" Final plot " 
       x[['y','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

      ## Concat
       #x_overlap = pd.concat([df[-N_points:], pred], axis=1, join="inner")
       x_overlap = pd.concat([df, pred], axis=1, join="inner")
       print("After concat len(x_overlap)=",len(x_overlap))
       print(x_overlap)
       print(x_overlap.index)
       # https://realpython.com/pandas-merge-join-and-concat/
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       #header="final _overlap sorted"
       x_overlap[['y','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

       print("Join")
       #x_join = df[-N_points:].join(pred)
       x_join = df.join(pred)
       print("After join len(x_join)=",len(x_join))
       print(x_join)
       print(x_join.index)
       # https://realpython.com/pandas-merge-join-and-concat/
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       header="final _join"
       x_join[['y','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()
   

def  main():
  #number_of_hours=24*7*4 # 4 weeks
  #rng = pd.date_range('2015-02-24', periods=number_of_hours, freq='H')
  #df = pd.DataFrame({ 'Date': rng, 'y': f() }, index=rng) 
  #print(df)
  #print(df.index)
  n_days=10
  df = init_df('2015-02-24', n_days)
  useLags=False

  #df.plot(y="y")
  #plt.show() 
  #predict_xgboost(df, "constant", useLags)

  df = init_df('2015-02-24', n_days)
  y_sin(df, amplitude=0.5, period=1, const=100)
  df.plot(y="y", title="periodic + 100")
  plt.show()
  predict_xgboost(df, "periodic + 100", useLags)

  df = init_df('2015-02-24', n_days)
  y_sin(df, amplitude=1.0, period=1, const=5)
  df.plot(y="y", title="periodic + 5")
  plt.show()
  predict_xgboost(df, " periodic + 5", useLags)

  df = init_df('2015-02-24', n_days)
  y_linear(df, 1.0)
  df.plot(y="y", title="linear")
  plt.show()
  predict_xgboost(df, "linear", useLags)

  #print(  df.info() )
  #df.plot(y="hours_from_start", title="hours from start")
  #plt.show()

  #return




  y_sin_and_linear(df, sin_amplitude=4, sin_period=10, k_linear=1, a_linear=1)
  df.plot(y="y", title="linear + sin()")
  plt.show()
  predict_xgboost(df, "sin and linear", useLags)

  y_sin_and_linear(df, sin_amplitude=1, sin_period=2, k_linear=0, a_linear=8)
  df.plot(y="y", title="linear + sin() again")
  plt.show()
  comment="linear + sin() again"
  predict_xgboost(df, comment, useLags)
 
  #


if __name__ == "__main__":
  use_lagged()
  #main()

