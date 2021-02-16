import sys
import argparse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import ( mean_absolute_error, mean_squared_error, make_scorer )
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, scale

from statsmodels.tsa.stattools import pacf, acf

# Database connection
import datastore

import xgboost
from xgboost import plot_importance, plot_tree
#import xgboost_autotune 

import xgb_autotune 

DEBUG=False
#---------------
def input_cmd():
#---------------
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--steps",
                        type=int,
                        default=48,
                        help="The number of forecasting hours")

    parser.add_argument("-c", "--company",
                        type=int,
                        default=3659,
                        help="The company")                    

    parser.add_argument("-f", "--file", 
                        type=str,
                        help="The file with 2 columns: date and value")

    parser.add_argument("-b", "--begin", 
                        type=str,
                        help="The start date in format YYYY-MM-DD")

    parser.add_argument("-e", "--end", 
                        type=str,
                        help="The end date in format YYYY-MM-DD")                    

    parser.add_argument("-t", "--table", 
                        type=str,
                        default="jangle_traffic_total", choices=['jangle_traffic_total', 'radius_traffic_total'],
                        help="The table")

    args = parser.parse_args()
    return args



def xxxfit_parameters(initial_model, initial_params_dict, X_train, y_train, min_loss, scoring, n_folds=5, iid=False):
    ### initial check
    available_models = ['XGBRegressor', 'GradientBoostingRegressor', 'LGBMRegressor']
    assert (type(initial_params_dict) is dict)
    assert (initial_model.__class__.__name__ in available_models)

    model=initial_model
    available_params = list(model.get_params().keys())
    # domain parameters, which will be used if no parameters provided by user
        # 1. n_estimators- should be quite low, in ranparamsge [40-120] (should be fast to checm many parameters, n_estimators will be fine-tuned later)
             # if optimal is 20, you might want to try lowering the learning rate to 0.05 and re-run grid search
             # learning rate-  0.05-0.2 powinno działać na początku
             # for LightGmax_depthBM n_estimators: must be infinite (like 9999999) and use early stopping to auto-tune (otherwise overfitting)
        # 2. num leaves- too much will lead to overfitting
             # min_samples_split: This should be ~0.5-1% of min_split_gaintotal values.
             # min_child_weight:  (sample size / 1000), nevfor p_name, p_array in params_dict.items():ertheless depedns on dataset and loss
        # 3. min_samples_leaf : a small value because of imbalanced classes, zrób kombinacje z 5 najlepszymi wartościami min_samples_split
        # 4. max_features = ‘sqrt’ : Its a general thumb-rule to start with square root.
        # others:param_pair = {'n_estimators': [final_params['n_estimators'] * n], 'learning_rate' : [final_params['learning_rate'] / n]}
             # is_unbalance: false (make your own weighting with scale_pos_weight)
             # Scale_pos_weight is the ratio of number of negative class to the positive class. Suppose, the dataset has 90 observations of negative class and 10 observations of positive class, then ideal value of scale_pos_Weight should be 9

    domain_params_dicts = [{'n_estimators': [30, 50, 70, 100, 150, 200, 300]},
                            {'max_depth': [3, 5, 7, 9], 'min_child_weight': [0.001, 0.1, 1, 5, 10, 20], 'min_samples_split': [1,2,5,10,20,30], 'num_leaves': [15, 35, 50, 75, 100,150]},
                            {'gamma': [0.0, 0.1, 0.2, 0.3, 0.4, 0.5], 'min_samples_leaf': [1,2,5,10,20,30], 'min_child_samples': [2,7,15,25,45], 'min_split_gain': [0, 0.001, 0.1, 1,5, 20]},
                            {'n_estimators': [30, 50, 70, 100, 150, 200, 300],  'max_features': range(10,25,3)},
                            {'subsample': [i/10 for i in range(4,10)], 'colsample_bytree': [i/10 for i in range(4,10)], 'feature_fraction': [i/10 for i in range(4,10)]},
                            {'reg_alpha':[1e-5, 1e-2, 0.1, 1, 25, 100], 'reg_lambda':[1e-5, 1e-2, 0.1, 1, 25, 100]}]

    # iterate over parameter anmes from domain_params_dicts, and adjust parameter value from following dictionaries
    for params_dict in domain_params_dicts:
        params ={}
        for p_name, p_array in params_dict.items():
            if (p_name in available_params):
                params[p_name] = set_initial_params(initial_params_dict, p_name, p_array)

        # save new best parameters
        best_params = find_best_params(model, params, X_train, y_train, min_loss, scoring, n_folds, iid).best_params_
        final_params = copy(model.get_params())
        model = update_model_params(model, final_params, best_params)

    # finally adjust pair (n_estimators, learning_rate)
    try:
        best_score = None
        for n in [1, 2, 4, 8, 15, 25]:
            param_pair = {'n_estimators': [final_params['n_estimators'] * n], 'learning_rate' : [final_params['learning_rate'] / n]}
            print('prediction for: ', param_pair)
            clf = GridSearchCV(model, param_pair, scoring=scoring, verbose=0, cv = n_folds, refit=True,  iid=iid)
            clf.fit(X_train, y_train)
            new_score = scoring._score_func(clf.predict(X_train), y_train) # calculate new metric_value

            # save parameters, if they give better results
            best_param_pair = param_pair
            if best_score is None:
                best_score = new_score
            elif scoring.__dict__['_sign'] == 1: # for score where greater is better
                if new_score - best_score >= min_loss:
                    best_score = new_score
                    best_param_pair = param_pair
            elif scoring.__dict__['_sign'] == -1:# for score where lower is better
                if new_score - best_score <= min_loss:
                    best_score = new_score
                    best_param_pair = param_pair
            print ('best score', best_score)
        best_param_pair = convert_dict_of_arrays(best_param_pair)
        model = update_model_params(model, final_params, best_param_pair)
    except:
        pass
    model.fit(X_train, y_train)

    return model

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

    if DEBUG:
       plt.plot(y)
       plt.plot(trend)
       plt.show()
    
    new_s = pd.Series( s.values - trend, s.index)
    print(new_s)

    print("-----new_s.index")
    print(new_s.index)

    print("------new_s.values")
    print(new_s.values)

    if DEBUG:
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
        shift: 3 shifts per day of 8 hours
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
    features["month"] = data.index.month
    features["shift"] = pd.Series(data.index.map(get_shift))
    # TODO - instead shift above is it better to have 3 features: night, day, evening 
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

     #fitted_model = xgboost_autotune.fit_parameters(
     fitted_model = xgb_autotune.fit_parameters(    
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
def multi_direct(c_target, f_steps):
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
    fcast_xgb[fcast_xgb < 0] = 0 
    print("--- multi_direct() final forecast=")
    print(fcast_xgb)

    if DEBUG:
       try:
         plot_importance(model_detrended, height=0.9)
         plt.show()
       except:
         print("error in plot_importance()")
 
#----------------------------------------------------
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.plot(c_target, color="blue", label="Original", linestyle='-', marker='o')
    
    ax.plot(fcast_xgb, color="green", label="Direct forecast", linestyle='-', marker='o')
    ax.set_title(f"{f_steps} hours forecast")
    ax.legend()
    plt.show()

#---------------
def main():
#---------------
    args = input_cmd()

    # get data
    try:
       company = args.company
       table = args.table
       begin = args.begin
       end = args.end
       fname = args.file
       f_steps = args.steps
       
       
       print(company)
       print(table)
       print(begin)
       print(end)
       print(fname)
       print(f_steps)


    except:
       print ("Error")

   
    if fname:  
        print ("reading from file not implemented")   
        #data = get_from_file(fname)
        #c_target = data["y"]
    elif begin and end and company >= 0:
        datastore.connect()
        start_date=begin #'2020-12-01'  # read from command line
        end_date=end #'2021-01-01'    # read from command line 
        #company=3659  # read from command line
        direction=None # read from command line
        # COMPANY_LIST=(3659,3116, 3666)
        #    for table in ['jangle_traffic_total', 'radius_traffic_total']:
        table='jangle_traffic_total' # read from command line
        data = get_data_from_db(table, start_date, end_date, company, direction)
        print(data)

        #  exit(1)
        s = data["y"]  # make series
        s.fillna(0, inplace=True)

        print(s)
        print(s.name)
        print(s.index)
        print(s.values)
        s.name='y'

    else:   
        print("simulate")
        #for shape in  ["random", "sin", "linear", "linear_and_sin"]:
        shape="linear_and_sin"
        s = generate_series(shape)
 
    multi_direct(s, f_steps) 

if __name__ == "__main__":
    main()
