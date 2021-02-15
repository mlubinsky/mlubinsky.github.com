import time
from datetime import datetime, timedelta
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import (TimeSeriesSplit, train_test_split)
#from sklearn.model_selection import GridSearchCV, cross_validate, ParameterGrid
from sklearn.metrics import make_scorer

# from sklearn.cross_validate import StratifiedKFold, KFold
# from sklearn.grid_search import ParameterGrid

import xgboost as xgb
from xgboost import plot_importance, plot_tree
import xgboost_autotune

# https://www.mikulskibartosz.name/xgboost-hyperparameter-tuning-in-python-using-grid-search/
# https://machinelearningmastery.com/auto-sklearn-for-automated-machine-learning-in-python/
#
PI=math.pi
print("PI", PI)

# https://www.kaggle.com/carlolepelaars/understanding-the-metric-rmsle
# https://github.com/dmlc/xgboost/blob/master/demo/guide-python/custom_rmsle.py

def rmsle(real, predicted):
    sum=0.0
    for x in range(len(predicted)):
        if predicted[x]<0 or real[x]<0: #check for negative values
            continue
        p = np.log(predicted[x]+1)
        r = np.log(real[x]+1)
        sum = sum + (p - r)**2
    return (sum/len(predicted))**0.5


def rmsle_2(h, y):
    return np.sqrt(np.square(np.log(h + 1) - np.log(y + 1)).mean())

# https://stackoverflow.com/questions/46202223/root-mean-log-squared-error-issue-with-scitkit-learn-ensemble-gradientboostingre
def rmsle_3(predt, dtrain):
        #y = dtrain.get_label()
        predt[predt < -1] = -1 + 1e-6
        elements = np.power(np.log1p(dtrain) - np.log1p(predt), 2)
        return  float(np.sqrt(np.sum(elements) / len(dtrain)))

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
def y_sin_and_cos(df, amplitude, period=1, const=5 ):
  df['y'] = const + amplitude * ( np.sin(df.index.hour * period * PI  /24.0 ) - 0.2 * np.cos(df.index.hour * period * PI  /24.0 ) )

def y_sin(df, amplitude, period=1, const=5 ):
   #for k in df.index.hour:
   #   print(k, np.sin(2* PI * k /24.0)  )
   #exit(1)

   df['y'] = const + amplitude * ( np.sin(df.index.hour * period * 2*PI  /24.0 ) )

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

#def f():
#   return 11


# https://medium.com/datadriveninvestor/an-introduction-to-grid-search-ff57adcc0998
# Hyperparmeter grid optimization

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

     concat = test.rename(columns={'y':'TEST'}) \
     .join( train.rename(columns={'y':'TRAIN'}) , how='outer')

     print("concat_join  len=", len(concat))
     print(concat)
     

     header=comment + ' Train: '+str(train_len) + ' points and Test: '+str(test_len) + " points"
     print(header)
     #exit(1)

     if show_details:
       concat.plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

     first_date=train.index.array[0]
     X_train, y_train = create_features(train, 'y', first_date, useLags)
     print("len(X_train)=", len(X_train), "len(Y_train)=",len(y_train))

     X_test,  y_test  = create_features(test,  'y', first_date, useLags)
     print("len(X_test)=", len(X_test), "len(Y_test)=",len(y_test))


     #find_hyperparams( X_train, y_train, X_test,  y_test )
     
     # https://www.kaggle.com/robikscube/time-series-forecasting-with-prophet

     rmlse_score = make_scorer( rmsle, greater_is_better=False)

     fitted_model = xgboost_autotune.fit_parameters(
        initial_model = xgb.XGBRegressor(),
        initial_params_dict = {},
        X_train = X_train,
        y_train = y_train,
        min_loss = 0.01,
        scoring = rmlse_score,  #  accuracy, #rmlse_score,
        n_folds=5
     )

#     model = xgb.XGBRegressor(
#       n_estimators = 1600 ,
#       random_state = 10 ,
#       objective='reg:squarederror',  #objective= 'reg:linear', #objective='binary:logistic',
#       learning_rate = 0.1,
#       min_child_weight=1,
#       gamma=0, 
#       subsample=0.8, 
#       colsample_bytree=0.8,
#       booster= 'gbtree', # booster:'gblinear',
#       max_depth = 35)

     # model = XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
     #    colsample_bynode=1, colsample_bytree=0.3, gamma=0,
     #    importance_type='gain', learning_rate=0.1, max_delta_step=0,
     #    max_depth=15, min_child_weight=1, missing=None, n_estimators=1000,
     #   n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
     #    reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
     #    silent=None, subsample=0.5, verbosity=1) 


    # model.fit(X_train, y_train,
    #    eval_set=[(X_train, y_train), (X_test, y_test)],
    #    early_stopping_rounds=500,
    #    verbose=False)

     # Feature importance
     if show_details:
       #plot_importance(model, height=0.9)
       try:
         plot_importance(fitted_model, height=0.9)
         plt.show()
       except:
         print("error in plot_importance()")

     print("Before Prediction")
     # test['Prediction'] = model.predict(X_test)
     test['Prediction'] = fitted_model.predict(X_test)

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

     return cc

def linear_detrend(df):
    print("detrend")
    #df["y"].plot()
    #plt.show()

    model=LinearRegression()
    #X = (df.index-df.index[0]).hours.reshape(-1,1)
    y = df["y"].values  # .reshape(-1,1)
    l = len(df)
    X = np.array(list(range(0, l))).reshape(-1,1)
    print("X len=", len(X))
    #print(X)
    print("y len=", len(y))
    #print(y)
    if len(y) != len(X):
        print("err")
        exit(1)
   
    model.fit(X , y )
    trend = model.predict(X)


#linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
#model.predict([[1], [7], [50]])

    plt.plot(y)
    plt.plot(trend)
    plt.show()

    df.rename(columns = {'y':'y_orig'}, inplace = True)

    df["y"] = df["y_orig"] - trend

    df[["y", "y_orig"]].plot() 
    plt.show()

    df.drop( columns=["y_orig"], inplace=True)

def init_df(start_day, number_of_days):
   number_of_hours=number_of_days * 24
   rng = pd.date_range(start_day, periods=number_of_hours, freq='H')
   df = pd.DataFrame({  'y': 1 }, index=rng)
   #print(df)
   return df

def use_lagged():
       N_points=5  

       n_days=1
       df = init_df('2015-02-24', n_days)
       y_sin(df, amplitude=0.5, period=1, const=100)

       head=df[:-N_points].copy()
       tail=df[-N_points:].copy()
       useLags=True
       comment = "Use lagged values n_days="+str(n_days)+" n_points="+str(N_points)

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
 
       header="final _join"
       x_join[['y','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()
   

def  main():
  n_days=10
  df = init_df('2015-02-24', n_days)
  useLags=False

  for const in [0]:   # [0,10]:
   if 0:
     df = init_df('2015-02-24', n_days) # to get rid of features?
     amplitude=1.0
     y_sin(df, amplitude=amplitude, period=1, const=const)
     header = "n_days="+str(n_days) +  " sin()  amplitude="+str(amplitude)+ " const="+str(const)
     df.plot(y="y", title=header )
     plt.show()
     predict_xgboost(df, header, useLags)

#--------   linear ---------
  if 0:
     df = init_df('2015-02-24', n_days)
     y_linear(df, 1.0)
#     df.plot(y="y", title="linear")
#     plt.show()
     linear_detrend(df)
     
     predict_xgboost(df, "linear", useLags)

#---   sin + linear ------
  for sin_amp in [10,30]:
    for sin_period in [1,30]:
       header= "sin() + linear sin_amplitude="+str(sin_amp) + "  sin_period="+str(sin_period)
       y_sin_and_linear(df, sin_amplitude=sin_amp, sin_period=sin_period, k_linear=1, a_linear=1)
       df.plot(y="y", title=header)
       plt.show()
       linear_detrend(df)
       df.plot(y="y", title="after detrend")
       plt.show()
       predict_xgboost(df, header, useLags)

if __name__ == "__main__":
  #use_lagged()
  main()

