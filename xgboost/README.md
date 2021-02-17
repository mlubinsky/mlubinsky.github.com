https://xgboost.readthedocs.io/en/latest/index.html

# Articles

https://filip-wojcik.com/talks/xgboost_forecasting_eng.pdf

https://towardsdatascience.com/forecasting-stock-prices-using-xgboost-a-detailed-walk-through-7817c1ff536a

https://medium.com/ai-trading-labs/forecasting-stock-prices-using-xgboost-part-2-2-5fa8ce843690

## Data preparation, categorical values:

https://machinelearningmastery.com/data-preparation-gradient-boosting-xgboost-python/

https://songxia-sophia.medium.com/two-machine-learning-algorithms-to-predict-xgboost-neural-network-with-entity-embedding-caac68717dea

https://stackoverflow.com/questions/34265102/xgboost-categorical-variables-dummification-vs-encoding

https://blog.dataiku.com/how-do-gradient-boosting-algorithms-handle-categorical-variables


## Hyperparams optimization:

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
``
