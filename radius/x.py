import time
from datetime import datetime, timedelta
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from sklearn.model_selection import GridSearchCV
from sklearn.metrics import ( mean_absolute_error, mean_squared_error, make_scorer )
#from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import (TimeSeriesSplit, train_test_split, cross_val_score)
#from sklearn.model_selection import GridSearchCV, cross_validate, ParameterGrid
#from sklearn.metrics import make_scorer
from sklearn.preprocessing import StandardScaler, scale
from statsmodels.tsa.stattools import pacf, acf

# from sklearn.cross_validate import StratifiedKFold, KFold
# from sklearn.grid_search import ParameterGrid

import xgboost as xgb
from xgboost import plot_importance, plot_tree

import xgboost_autotune  # https://github.com/SylwiaOliwia2/xgboost-AutoTune

# https://www.mikulskibartosz.name/xgboost-hyperparameter-tuning-in-python-using-grid-search/
# https://machinelearningmastery.com/auto-sklearn-for-automated-machine-learning-in-python/
#



#PI=math.pi
#print("PI", PI)

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




def direct( y, train_fn, lags, n_steps, step="1H",  params=None):
        
        """Multi-step direct forecasting using a machine learning model
        to forecast each time period ahead
        
        Parameters
        ----------
        y: pd.Series holding the input time-series to forecast
        train_fn: a function for training the model which returns as output the trained model
                  cross-validation score and test score
        params: additional parameters for the training function
        
        Returns
        -------
        fcast_values: pd.Series with forecasted values indexed by forecast horizon dates    
        """
        
        def one_step_features(date, step):

            # features must be obtained using data lagged 
            # by the desired number of steps (the for loop index)
            tmp = y[y.index <= date]       
            lags_features = create_lag_features(tmp, lags=lags)
            ts_features = create_ts_features(tmp)
            if lags_features.empty:
                print("-----  no lags--------")
            
            features = ts_features.join(lags_features, how="outer").dropna()
            #else:    
            #    features = ts_features.copy()

            # build target to be ahead of the features built 
            # by the desired number of steps (the for loop index)
            target = y[y.index >= features.index[0] + pd.Timedelta(hours=step)]
            assert len(features.index) == len(target.index)
            
            return features, target
            
        params = {} if params is None else params
        fcast_values = []
        fcast_range = pd.date_range(y.index[-1] + pd.Timedelta(hours=1), 
                                    periods=n_steps, #   self.n_steps, 
                                    freq=step # self.step
        )
        fcast_features, _ = one_step_features(y.index[-1], 0)
                
        for s in range(1, n_steps+1):  # self.n_steps+1):
            
            last_date = y.index[-1] - pd.Timedelta(hours=s)
            features, target = one_step_features(last_date, s)
            
            model, cv_score, test_score = train_fn(features, target, **params) 
                
            # use the model to predict s steps ahead
            predictions = model.predict(fcast_features)        
            fcast_values.append(predictions[-1])
                    
        return pd.Series(index=fcast_range, data=fcast_values)




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
#------------------------
def linear_detrend(df):
#------------------------    
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
#------------------------------------------
def init_df(start_day, number_of_days):
#-----------------------------------------    
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


def generate_series(signal="random", start_day='2020-12-01', number_of_days=5, amplitude=1, freq=1):
     PI = 3.14159
     number_of_hours=number_of_days * 24
     rng = pd.date_range(start_day, periods=number_of_hours, freq='H')
     #df = pd.DataFrame({ 'Date': rng, 'y': 1 }, index=rng)
     if signal == "random":
         s = pd.Series(np.random.randn(number_of_hours), index=rng, name='y')
     elif signal == "sin":
         const =  0

         s = pd.Series( const + amplitude * ( np.sin(rng.hour * freq * PI  /12.0 )  ), index=rng, name='y')
         #s = pd.Series( const + amplitude * ( np.sin(df.index.hour * period * PI  /24.0 ) - 0.2 * np.cos(df.index.hour * period * PI  /24.0 ) )
   
     elif signal == "linear":
     # def y_sin_and_linear(df, sin_amplitude, sin_period, k_linear, a_linear):

      first_timepoint=rng[0]
      intersect=0.0
      slope=1.0

      hours_from_start =  (rng - first_timepoint).astype('timedelta64[h]').astype(int)
      s = pd.Series( intersect + slope * hours_from_start, index=rng, name="y" )
      # + sin_amplitude * np.sin(df.index.hour * sin_period * PI  /24.0 )

     elif signal == "linear_and_sin":
     # def y_sin_and_linear(df, sin_amplitude, sin_period, k_linear, a_linear):

      first_timepoint=rng[0]
      intersect=0.0
      slope=1.0
      amplitude=10
      hours_from_start =  (rng - first_timepoint).astype('timedelta64[h]').astype(int)
      s = pd.Series( 
         intersect + slope * hours_from_start + amplitude * ( np.sin(rng.hour * freq * PI  /12.0 )  ), 
         index=rng, 
         name="y" 
      )

     else:
        print("signal=", signal, " not implemented")
        exit(1)

     print("series=")
     print(s)
     #print ("series index=")
     #print(s.index)
     s.plot(title=signal)
     plt.show()
     #exit(1)
     return s

# https://en.wikipedia.org/wiki/Mean_absolute_percentage_error
# https://en.wikipedia.org/wiki/Mean_absolute_scaled_error
# MAPE computation

#----------------------------
def mape(y, yhat, perc=True):
#----------------------------    
    n = len(yhat.index) if type(yhat) == pd.Series else len(yhat)    
    mape = []
    for a, f in zip(y, yhat):
        # avoid division by 0
        if f > 1e-9 and a !=0:
            mape.append(np.abs((a - f)/a))
    mape = np.mean(np.array(mape))
    return mape * 100. if perc else mape

#----------------------------
def mape_2(y, yhat, perc=False):
#----------------------------    
    n = len(yhat.index) if type(yhat) == pd.Series else len(yhat)    
    mape = []
    for a, f in zip(y, yhat):
        # avoid division by 0
        #if f > 1e-9 and a !=0:
        mape.append(np.abs((a - f)))

    mape = np.mean(np.array(mape))
    return mape * 100. if perc else mape


mape_scorer = make_scorer(mape, greater_is_better=False)

def get_features(y, f_lags=True, f_endog=False, lags=None):

    """
    Create the feature set for the time series

    Parameters
    ----------
    y: pd.Series with the target time series
    f_lags: boolean switch for turning on lags features
    f_endog: boolean switch for turning on endogenous features
    lags: optional list of lags to create the lag features for

    Returns
    -------
    features: pd.DataFrame with the feature set
    target: pd.Series holding the target time series with the same index as the features
    """

    features = pd.DataFrame()

    ts = create_ts_features(y)
    features = features.join(ts, how="outer").dropna()

    if f_lags:
        lags = create_lag_features(y, lags=lags, thres=0.2)
        features = features.join(lags, how="outer").dropna()

    if f_endog:
        endog = create_endog_features(y)
        features = features.join(endog, how="outer").dropna()
    
    target = y[y.index >= features.index[0]]

    return features, target

def create_ts_features(data):
    
    def get_shift(row):
        """
        Factory working shift: 3 shifts per day of 8 hours
        """
        if 6 <= row.hour <= 14:
            return 2
        elif 15 <= row.hour <= 22:
            return 3
        else:
            return 1
    
    features = pd.DataFrame()
    
    features["hour"] = data.index.hour
    features["weekday"] = data.index.weekday
    features["dayofyear"] = data.index.dayofyear
    features["is_weekend"] = data.index.weekday.isin([5, 6]).astype(np.int32)
    #features["weekofyear"] = data.index.weekofyear
    features["month"] = data.index.month
    features["season"] = (data.index.month%12 + 3)//3
    features["shift"] = pd.Series(data.index.map(get_shift))
    
    features.index = data.index
        
    return features

def create_lag_features(target, lags=None, thres=0.2):
    print("--- lags=None  create_lag_features lags=", lags)
    scaler = StandardScaler()
    features = pd.DataFrame()
                
    if lags is None:
        # PACF - partial autocorrelation functions.
        # consider lag features only when PACF is greater than 0.2 (5% relevance) to build the features
        try:
            partial = pd.Series(data=pacf(target, nlags=48))
            lags = list(partial[np.abs(partial) >= thres].index)

        except:
            print("error numpy.linalg.LinAlgError: Singular matrix")
            #return pd.DataFrame()
             

    df = pd.DataFrame()

    if not lags or len(lags) == 0 :
                print("no lags")  
                return df

    if 0 in lags:
        lags.remove(0) # do not consider itself as lag feature
    for l in lags:
        df[f"lag_{l}"] = target.shift(l)

    print("----  lags= --------")        
    print (lags)
    print("len df=",  len(df))
    print(df.columns)
    print("--------------")

    features = pd.DataFrame(scaler.fit_transform(df[df.columns]), 
                            columns=df.columns)

    features = df
    features.index = target.index
    
    return features


def forecast_split(data, n_steps=5, freq="1H"):
      """
       Returns
        t_target: pd.Series with the training data
        f_target: pd.Series with the forecast data
        fcast_range: pd.DateRange with the forecasting timestamps
      """

      # the complete time series
      c_target = data.copy()

      # data used for training
      date = c_target.index[-1] - pd.Timedelta(hours=n_steps)
      t_target = c_target[c_target.index <= date]

      # data used for forecasting
      f_target = c_target[c_target.index > date]
      fcast_initial_date = f_target.index[0]
      fcast_range = pd.date_range(fcast_initial_date, periods=n_steps, freq=freq)

      print(f"Full available time range: from {c_target.index[0]} to {c_target.index[-1]}")
      print(f"Training time range: from {t_target.index[0]} to {t_target.index[-1]}")
      print(f"Forecasting time range: from {fcast_range[0]} to {fcast_range[-1]}")

      return t_target, f_target, fcast_range
#------------------------
from functools import partial
import xgboost as xgb

# https://neptune.ai/blog/optuna-vs-hyperopt
#from hyperopt import fmin, tpe, hp, Trials, STATUS_OK, STATUS_FAIL
import hyperopt # import fmin, tpe, hp, Trials, STATUS_OK, STATUS_FAIL
from sklearn.model_selection import train_test_split

#  from linear import train_model, test_model
# https://github.com/madagra/energy-ts-analysis/blob/c892d595dc32a9dba081d1ef98504510621313e5/src/linear.py

def test_model(model, X_test, y_test):
    """
    Get the RMSE for a given model on a test dataset
    Parameters
    ----------
    model: a model implementing the standard scikit-learn interface
    X_test: pd.DataFrame holding the features of the test set
    y_test: pd.Series holding the test set target
    Returns
    -------
    test_score: the RMSE on the test dataset
    """
    
    predictions = model.predict(X_test)
    #test_score = mape(y_test.values, predictions)
    test_score = mape_2(y_test.values, predictions)
    return test_score

#-------------------------------------------------------------------
def train_autotune_model(model, X_train, y_train, **fit_parameters):
#-------------------------------------------------------------------
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

     return {
            "loss": rmlse_score,
            "status": 0,
            "model": fitted_model
     }

#-------------------------------------------------------------------
def train_hyperopt_model(model, X_train, y_train, **fit_parameters):
#-------------------------------------------------------------------
    """
    Train a model with time series cross-validation by returning
    the right dictionary to be used by hyperopt for optimization
    Parameters
    ----------
    model: a model implementing the standard scikit-learn interface
    X_train: pd.DataFrame holding the training features
    y_train: pd.Series holding the training target
    fit_parameters: dict with parameters to pass to the model fit function
    Returns
    -------
    Dictionary holding the resulting model, RMSE and final status of the training
    as required by hyperopt interface
    """

    try:

        model.fit(X_train, y_train, **fit_parameters)

        # cross validate using the right iterator for time series
        cv_space = TimeSeriesSplit(n_splits=5)
        cv_score = cross_val_score(model, 
                                   X_train, 
                                   y_train.values.ravel(), 
                                   cv=cv_space, 
                                   scoring=mape_scorer)

        mape = np.mean(np.abs(cv_score))
        return {
            "loss": mape,
            "status": hyperopt.STATUS_OK,
            "model": model
        }
        
    except ValueError as ex:
        return {
            "error": ex,
            "status": hyperopt.STATUS_FAIL
        }

def not_in_use_linear_model(features, target, model_cls=LinearRegression, test_size=0.2, params=None):
    """
    Full training and testing pipeline for linear regression model
    without hyperparameter optimization
    Parameters
    ----------
    features: pd.DataFrame holding the model features
    target: pd.Series holding the target values
    model_cls: model constructor from scikit-learn    
    test_size: the train/test split size
    params: additional parameters to pass to model constructor
    Returns
    -------
    model: the optimized linear regression model
    cv_score: the average RMSE coming from cross-validation
    test_score: the RMSE on the test set
    """

    X_train, X_test, y_train, y_test = train_test_split(features, 
                                                        target, 
                                                        test_size=test_size,
                                                        shuffle=False)
    params = params if params is not None else {}
    model = model_cls(**params)
    res = train_model(model, X_train, y_train)
    cv_score = res["loss"]
    test_score = test_model(res["model"], X_test, y_test)
    return model, cv_score, test_score

def train_xbg_model(params, X_train, y_train):
    """
    Train a XGBoost model with given input parameters
    
    Parameters
    ----------
    params: dict with parameters to be passed to model constructor
    X_train: pd.DataFrame holding the training features
    y_train: pd.Series holding the training target
    
    Returns
    -------
    Dictionary holding the resulting model, MAPE score and final status of the training
    as required by hyperopt interface    
    """

    n_estimators = int(params["n_estimators"])
    max_depth= int(params["max_depth"])

    model = xgb.XGBRegressor(n_estimators=n_estimators, 
                             max_depth=max_depth, 
                             learning_rate=params["learning_rate"],
                             subsample=params["subsample"])

    res = train_autotune_model(model, X_train, y_train)
                    #  ,
                    #  eval_set=[(X_train, y_train.values.ravel())],
                    #  early_stopping_rounds=50,
                    #  verbose=False)

    #res = train_hyperopt_model(model, X_train, y_train,
    #                  eval_set=[(X_train, y_train.values.ravel())],
    #                  early_stopping_rounds=50,
    #                  verbose=False)
    return res

def optimize_xgb_model(X_train, y_train, max_evals=50, verbose=False):
    """
    Run Bayesan optimization to find the optimal XGBoost algorithm
    hyperparameters.
    
    Parameters
    ----------
    X_train: pd.DataFrame with the training set features
    y_train: pd.Series with the training set targets
    max_evals: the maximum number of iterations in the Bayesian optimization method
    verbose: if True print the best output parameters
    Returns
    -------
    best: dict with the best parameters obtained
    trials: a list of hyperopt Trials objects with the history of the optimization
    """
    #from hyperopt import fmin, tpe, hp, Trials, STATUS_OK, STATUS_FAIL
    space = {
        "n_estimators": hyperopt.hp.quniform("n_estimators", 100, 1000, 10),
        "max_depth": hyperopt.hp.quniform("max_depth", 1, 8, 1),
        "learning_rate": hyperopt.hp.loguniform("learning_rate", -5, 1),
        "subsample": hyperopt.hp.uniform("subsample", 0.8, 1),
        "gamma": hyperopt.hp.quniform("gamma", 0, 100, 1)
    }

    objective_fn = partial(train_xbg_model, 
                           X_train=X_train, 
                           y_train=y_train)
    
    trials = hyperopt.Trials()

    try:
       best = hyperopt.fmin(fn=objective_fn,
                space=space,
                algo=hyperopt.tpe.suggest,
                max_evals=max_evals,
                trials=trials)
    except:
        print("Exception hyperopt.exceptions.AllTrialsFailed")
        exit(0)

    if verbose:
        print(f"""
        Best parameters:
            learning_rate: {best["learning_rate"]} 
            n_estimators: {best["n_estimators"]}
            max_depth: {best["max_depth"]}
            sub_sample: {best["subsample"]}
            gamma: {best["gamma"]}
        """)

    return best, trials


def xgboost_model(features, target, test_size=0.2, max_evals=10):
    """
    Full training and testing pipeline for XGBoost ML model with
    hyperparameter optimization using Bayesian method
    Parameters
    ----------
    features: pd.DataFrame holding the model features
    target: pd.Series holding the target values
    max_evals: maximum number of iterations in the optimization procedure
    Returns
    -------
    model: the optimized XGBoost model
    cv_score: the average RMSE coming from cross-validation
    test_score: the RMSE on the test set
    """

    X_train, X_test, y_train, y_test = train_test_split(features, 
                                                        target, 
                                                        test_size=test_size,
                                                        shuffle=False)

    use_hyperopt=False

    if use_hyperopt:
        best, trials = optimize_xgb_model(X_train, y_train, max_evals=max_evals)
        res = train_xbg_model(best, X_train, y_train)
        model = res["model"]
        cv_score = min([f["loss"] for f in trials.results if f["status"] == hyperopt.STATUS_OK])
        test_score = test_model(model, X_test, y_test)
        return model, cv_score, test_score

    else:
        
        res = train_autotune_model(None, X_train, y_train)
        model = res["model"]
        return model, 0.0, 0.0
#-----------------------
def multi_direct(c_target, f_steps=5):
#   https://github.com/madagra/energy-ts-analysis/blob/c892d595dc32a9dba081d1ef98504510621313e5/src/main.py
    print("-- multi_direct() ---")

    t_target, f_target, fcast_range = forecast_split(c_target, n_steps=f_steps)
    features, target = get_features(t_target)

    print("--- multi_direct() len(t_target) =", len(t_target), \
                                  "len(f_target)=", len(f_target), \
                                  "len(fcast_range)=", len(fcast_range) \
    )                      
    print("--- multi_direct() features---")
    #print(features.info())
    print(features)

    print("-- multi_direct() target---")
    #print(target.info())
    print(target)

    lags = [int(f.split("_")[1]) for f in features if "lag" in f]
    print("--- multi_direct() main lags=", lags)
    #exit(1)
    t_target_detrended, model_detrended = detrend(t_target)
    #fcast_xgb = direct(t_target, xgboost_model, lags, f_steps)
    fcast_xgb_detrended = direct(t_target_detrended, xgboost_model, lags, f_steps)

    start=len(t_target)
    end = start + len(f_target)
    X = np.array(list(range(start, end))).reshape(-1,1)
    fcast_xgb = model_detrended.predict(X) + fcast_xgb_detrended
    print("--- multi_direct() final forecast=")
    print(fcast_xgb)
    #exit(1)
#----------------------------------------------------
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.plot(c_target, color="blue", label="Original", linestyle='-', marker='o')
    # ax.plot(rec_fcast, color="red", label="Recursive forecast")
    ax.plot(fcast_xgb, color="green", label="Direct forecast", linestyle='-', marker='o')
    ax.set_title(f"{f_steps} hours forecast")
    ax.legend()
    plt.show()



#------------------------
def detrend(s):
#------------------------    
    print("detrend")
    #df["y"].plot()
    #plt.show()

    
    #X = (df.index-df.index[0]).hours.reshape(-1,1)
    y = s.values  # .reshape(-1,1)
    l = len(s)
    X = np.array(list(range(0, l))).reshape(-1,1)

    #X = (s.index -  df.index[0]).days + s.index.hour
    
    
    print("X len=", len(X))
    print(X)
    #X = (s.index.year * 100000 + s.index.dayofyear * 100 + s.index.hour) 
    #X = X.values.reshape(-1,1)
    print("y len=", len(y))
    #print(y)
    if len(y) != len(X):
        print("err")
        exit(1)
   
    model=LinearRegression().fit(X , y )
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    trend = model.predict(X)
   
   #linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
#model.predict([[1], [7], [50]])

    plt.plot(y)
    plt.plot(trend)
    plt.show()
    
    new_s = pd.Series( s.values - trend, s.index)
    print(new_s)

    print("-----new_s.index")
    print(new_s.index)

    print("------new_s.values")
    print(new_s.values)
    new_s.plot(title="detrended!!!")
    plt.show()

    return new_s, model
    #new_s =  s.copy()
    #new_s.replace(trend)
    #df.rename(columns = {'y':'y_orig'}, inplace = True)

    #df["y"] = df["y_orig"] - trend

    #df[["y", "y_orig"]].plot() 
    #plt.show()

    #df.drop( columns=["y_orig"], inplace=True)
#-------------------------
if __name__ == "__main__":
#-------------------------
  
  #detrend(s)
  #use_lagged()
  #main()
  for shape in  ["random", "sin", "linear", "linear_and_sin"]:
  #for shape in  [  "linear", "linear_and_sin"]:
    s = generate_series(shape)
    #s_detrended , model = detrend(s)
    multi_direct(s)