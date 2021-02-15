## Data preparation, categorical values:

https://machinelearningmastery.com/data-preparation-gradient-boosting-xgboost-python/

https://songxia-sophia.medium.com/two-machine-learning-algorithms-to-predict-xgboost-neural-network-with-entity-embedding-caac68717dea

https://stackoverflow.com/questions/34265102/xgboost-categorical-variables-dummification-vs-encoding

https://blog.dataiku.com/how-do-gradient-boosting-algorithms-handle-categorical-variables


## Hyperparams optimization:

https://neptune.ai/blog/optuna-vs-hyperopt

https://github.com/SylwiaOliwia2/xgboost-AutoTune. 
```
here the fix is required for the latest version of sklearn: remove iid in
file /Users/miclub01/anaconda3/lib/python3.7/site-packages/xgboost_autotune.py
 
 100     clf = GridSearchCV(model, parameters, scoring=scoring, verbose=0, cv = n_folds, refit=True) #, iid=iid)
``
