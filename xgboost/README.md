https://xgboost.readthedocs.io/en/latest/index.html

```
from sklearn.metrics import mean_squared_error, mean_absolute_error

mean_squared_error(y_true=dfs_test[‘y’],
y_pred=dfs_test[‘y_Prediction’])

mean_absolute_error(y_true=dfs_test[‘y’],
y_pred=dfs_test[‘y_Prediction’])
```


https://github.com/NGYB/Stocks/blob/master/StockReturnsPrediction_fh21/StockReturnsPrediction_v3_xgboost.ipynb  from here:
```
def get_mape(y_true, y_pred): 
    """
    Compute mean absolute percentage error (MAPE)
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def get_wape(y_true, y_pred): 
    """
    Compute weighted absolute percentage error (WAPE)
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return sum(np.abs(y_true - y_pred)) / sum(y_true) * 100

def get_mae(a, b):
    """
    Comp mean absolute error e_t = E[|a_t - b_t|]. a and b can be lists.
    Returns a vector of len = len(a) = len(b)
    """
    return np.mean(abs(np.array(a)-np.array(b)))

def get_rmse(a, b):
    """
    Comp RMSE. a and b can be lists.
    Returns a scalar.
    """
    return math.sqrt(np.mean((np.array(a)-np.array(b))**2))
 ```   

https://github.com/julianikulski/bike-sharing/blob/master/bike_sharing_demand.ipynb
```
# root mean squared error
print('XGBoost: Average RMSE train data:', 
      sum([np.sqrt(-1 * x) for x in scores_xgb['train_neg_mean_squared_error']])/len(scores_xgb['train_neg_mean_squared_error']))
print('XGBoost: Average RMSE test data:', 
      sum([np.sqrt(-1 * x) for x in scores_xgb['test_neg_mean_squared_error']])/len(scores_xgb['test_neg_mean_squared_error']))

# mean absolute error
print('XGBoost: Average MAE train data:', 
      sum([(-1 * x) for x in scores_xgb['train_neg_mean_absolute_error']])/len(scores_xgb['train_neg_mean_absolute_error']))
print('XGBoost: Average MAE test data:', 
      sum([(-1 * x) for x in scores_xgb['test_neg_mean_absolute_error']])/len(scores_xgb['test_neg_mean_absolute_error']))

# root mean squared log error
print('XGBoost: Average RMSLE train data:', 
      sum([np.sqrt(-1 * x) for x in scores_xgb['train_neg_mean_squared_log_error']])/len(scores_xgb['train_neg_mean_squared_log_error']))
print('XGBoost: Average RMSLE test data:', 
      sum([np.sqrt(-1 * x) for x in scores_xgb['test_neg_mean_squared_log_error']])/len(scores_xgb['test_neg_mean_squared_log_error']))
```

## Articles

https://filip-wojcik.com/talks/xgboost_forecasting_eng.pdf

<https://www.kaggle.com/robikscube/tutorial-time-series-forecasting-with-xgboost>

## Article with code

https://towardsdatascience.com/forecasting-stock-prices-using-xgboost-a-detailed-walk-through-7817c1ff536a

https://medium.com/ai-trading-labs/forecasting-stock-prices-using-xgboost-part-2-2-5fa8ce843690

https://github.com/NGYB/Stocks/blob/master/StockReturnsPrediction_fh21/StockReturnsPrediction_v4_xgboost.ipynb

https://github.com/NGYB/Stocks/blob/master/StockReturnsPrediction_fh21/StockReturnsPrediction_v3_xgboost.ipynb


model_xgb = xgb.XGBRegressor(random_state=42)

https://github.com/julianikulski/bike-sharing/blob/master/bike_sharing_demand.ipynb

## Data preparation, categorical values:

https://machinelearningmastery.com/data-preparation-gradient-boosting-xgboost-python/

https://songxia-sophia.medium.com/two-machine-learning-algorithms-to-predict-xgboost-neural-network-with-entity-embedding-caac68717dea

https://stackoverflow.com/questions/34265102/xgboost-categorical-variables-dummification-vs-encoding

https://blog.dataiku.com/how-do-gradient-boosting-algorithms-handle-categorical-variables


## Hyperparams optimization

https://machinelearningmastery.com/tune-xgboost-performance-with-learning-curves/

https://aiinpractice.com/xgboost-hyperparameter-tuning-with-bayesian-optimization/

https://habr.com/ru/company/skillfactory/blog/549474/

https://towardsdatascience.com/hyperparameter-optimization-in-python-part-0-introduction-c4b66791614b

https://towardsdatascience.com/hyperparameter-optimization-in-python-part-2-hyperopt-5f661db91324

https://habr.com/ru/post/542624/. hyperopt

https://neptune.ai/blog/optuna-vs-hyperopt

hyperopt.exceptions.AllTrialsFailed

https://github.com/SylwiaOliwia2/xgboost-AutoTune. 
```
here the fix is required for the latest version of sklearn: remove iid in
file /Users/miclub01/anaconda3/lib/python3.7/site-packages/xgboost_autotune.py
 
 100     clf = GridSearchCV(model, parameters, scoring=scoring, verbose=0, cv = n_folds, refit=True) #, iid=iid)
```


### XGBoost LightGBM 

https://bradleyboehmke.github.io/HOML/gbm.html#xgboost

https://www.shirin-glander.de/2018/11/ml_basics_gbm/

```
conda list | grep xgboost
_py-xgboost-mutex         2.0                       cpu_0
libxgboost                0.90                 h0a44026_1
py-xgboost-cpu            0.90                     py37_1


conda install -c conda-forge xgboost
Collecting package metadata (current_repodata.json): done
Solving environment: |
The environment is inconsistent, please check the package plan carefully
The following packages are causing the inconsistency:

  - defaults/osx-64::py-xgboost-cpu==0.90=py37_1
  
The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    certifi-2020.12.5          |   py37hf985489_1         143 KB  conda-forge
    libxgboost-1.1.1           |       h4a8c4bd_0         1.9 MB  conda-forge
    py-xgboost-1.1.1           |   py37hc8dfbb8_0         1.0 MB  conda-forge
    py-xgboost-cpu-1.1.1       |   py37hc8dfbb8_0          10 KB  conda-forge
    xgboost-1.1.1              |   py37h570ac47_0          11 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         3.1 MB  


pip list | grep xgboost
xgboost                            1.31

(mljar) virtualenv

pip list | grep xgboost
xgboost            1.2.0
```

