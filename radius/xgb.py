import sys
import argparse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#from utils import get_dataset, forecast_split, mape

#from forecaster import Forecaster
#from features import get_features
#from features import TargetTransformer

#from xgb import xgboost_model
#from linear import linear_model
from sklearn.metrics import ( mean_absolute_error, mean_squared_error, make_scorer )
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, scale
from statsmodels.tsa.stattools import pacf, acf

# Database connection
import datastore

import xgboost
import xgboost_autotune 

def input_cmd():
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--steps",
                        type=int,
                        default=48,
                        help="The number of forecasting steps")

    parser.add_argument("-f", "--fcast", 
                        type=str,
                        default="recursive", choices=["direct", "recursive"],
                        help="The type of forecasting")

    parser.add_argument("-l", "--load", 
                        type=str,
                        default="C4", choices=["C1", "C2", "C3", "C4"],
                        help="The load to predict")

    args = parser.parse_args()
    return args
#-------------------------------------------------------------------------
def query(sql):
#-------------------------------------------------------------------------
  datastore.start_transaction(readonly=True)
  d=datastore.query(sql)
  datastore.commit()
  return d
#-------------------------------------------------------------------------
def sql_hourly_traffic(table, start, end, company, direction=None):
#-------------------------------------------------------------------------

  timescale= '%%Y-%%m-%%d %%H'
  if not direction:
    filter="1=1"
  else:
    filter="direction="+str(direction) 

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   SUM(bytes)  / (1024.0 * 1024.0)   as y
   FROM {table}
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company =  {company}
   and {filter}
   GROUP BY date
   ORDER BY date
  """

  return SQL
#-------------------------------------------------------------------------
def get_data_from_db(table, start_date, end_date, company, direction=None):
#-------------------------------------------------------------------------

  sql =  sql_hourly_traffic(table, start_date, end_date, company, direction)
  print(sql)
  df = query(sql)
  date_range  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
  df['date'] = pd.to_datetime(df['date'])
  df.set_index('date', inplace=True)
  df=df.reindex(date_range)
  # TODO fillna(0)
  return df


#-------------------------------------------------------------------------
def generate_series(signal="random", start_day='2020-12-01', number_of_days=5, amplitude=1, freq=1):
#-------------------------------------------------------------------------

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


#------------------------
def detrend(s):
#------------------------    
    print("detrend")
    y = s.values  # .reshape(-1,1)
    l = len(s)
    X = np.array(list(range(0, l))).reshape(-1,1)

    print("X len=", len(X))
    print(X)

    #print("y len=", len(y))
    #print(y)
    #if len(y) != len(X):
    #    print("err")
    #    exit(1)
   
    model=LinearRegression().fit(X , y )
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    trend = model.predict(X)


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

#-----------------------------------------------
def forecast_split(data, n_steps=5, freq="1H"):
#-----------------------------------------------    
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

#---------------------------------------------------------
def get_features(y, f_lags=True, f_endog=False, lags=None):
#---------------------------------------------------------
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
#-----------------------------
def create_ts_features(data):
#-----------------------------    
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
#----------------------------------------------------
def create_lag_features(target, lags=None, thres=0.2):
#----------------------------------------------------    
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

#---------------------------------------------------------------
def direct( y, train_fn, lags, n_steps, step="1H",  params=None):
#---------------------------------------------------------------        
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



# https://github.com/dmlc/xgboost/blob/master/demo/guide-python/custom_rmsle.py
#--------------------------
def rmsle(real, predicted):
#--------------------------    
    sum=0.0
    for x in range(len(predicted)):
        if predicted[x]<0 or real[x]<0: #check for negative values
            continue
        p = np.log(predicted[x]+1)
        r = np.log(real[x]+1)
        sum = sum + (p - r)**2
    return (sum/len(predicted))**0.5

#-------------------------------------------------------------------
def train_autotune_model(model, X_train, y_train, **fit_parameters):
#-------------------------------------------------------------------
     rmlse_score = make_scorer( rmsle, greater_is_better=False)

     fitted_model = xgboost_autotune.fit_parameters(
        initial_model = xgboost.XGBRegressor(),
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
def xgboost_model(features, target, test_size=0.2, max_evals=10):
#-------------------------------------------------------------------    
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

    res = train_autotune_model(None, X_train, y_train)
    model = res["model"]
    return model, 0.0, 0.0
#------------------------------------
def multi_direct(c_target, f_steps=5):
#------------------------------------    
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

#---------------
def main():
#---------------
    args = input_cmd()

    # get data
    load = args.load
    f_steps = args.steps

    FROM_FILE=1
    FROM_DATABASE=2
    FROM_SIMULATE=3

    datasource = FROM_SIMULATE
   
    if datasource == FROM_FILE:  
        print ("not implemented")   
        #data = get_from_file(fname)
        #c_target = data["y"]
    elif datasource == FROM_DATABASE:
        datastore.connect()
        start_date='2020-12-01'  # read from command line
        end_date='2021-01-01'    # read from command line 
        company=3659  # read from command line
        direction=None # read from command line
        # COMPANY_LIST=(3659,3116, 3666)
        #    for table in ['jangle_traffic_total', 'radius_traffic_total']:
        table='jangle_traffic_total' # read from command line
        data = get_data_from_db(table, start_date, end_date, company, direction)
        print(data)
        #  exit(1)
        s = data["y"]  # make series
    elif  datasource == FROM_SIMULATE:   #-- simulate
        print("simulate")
        #for shape in  ["random", "sin", "linear", "linear_and_sin"]:
        shape="linear_and_sin"
        s = generate_series(shape)
         
    else:
        print("datasource is not provided")
        exit(1)

    multi_direct(s) 

if __name__ == "__main__":
    main()
