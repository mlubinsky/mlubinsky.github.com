https://developers.google.com/machine-learning/crash-course/

### Plotting
Seaborn pairplot
Heatmap
Cross-correlation plot

### Sampling

https://medium.com/@tzjy/4-typical-sampling-methods-you-need-for-data-science-jobs-python-code-included-b003feb6504b

### Quantile
https://medium.com/@tzjy/a-gentle-intro-to-quantile-regression-5f03b6bddae2

Quantiles are cut points dividing the range of a probability distribution into continuous intervals with equal probabilities.
A cut at any given percent is a percentile, the most common cut being the median (50th percentile). 
Quartiles are formed by 3 cuts (25th, 50th, and 75th percentiles), often used in box plots.

### Regularization
https://medium.com/@tzjy/the-true-reason-why-we-need-regularization-cec063696ca7
 Overfitting -  As the number of features approaches the number of observations, linear regression still “works”, but it starts giving fairly perverse results. 
 In particular, it results in a model that fails to generalize
We want to add bias to the model because of the bias-variance tradeoff 
https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff
  variance is the sensitivity of a model to the random noise in its training data (i.e. over-fitting), and bias and variance are naturally (inversely) related. Increasing one will always decrease the other, with regards to the overall generalization error (predictive accuracy on unseen data).

Regularization terms are of generally two different types, which are called L2 and L1. 
While L2 term is the Euclidean distance between the origin and the position in which model weights are situated in multi-dimensional space, 
L1 term refers to same thing except for the calculation method of the distance, 
which is actually manhattan distance. 
In the figure below, L2 and L1 regularization terms are demonstrated with loss functions of logistic regression and linear regression respectively.

### Model evaluation
https://arxiv.org/abs/1811.12808
Sebastian Raschka gave a very nice summary in his paper, Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning, of 4 model validation methods:
Performance estimation
- 2-way holdout method (train/test split)
- (Repeated) k-fold cross-validation without independent test set
- Model selection (hyperparameter optimization) and performance estimation
- 3-way holdout method (train/validation/test split)
- (Repeated) k-fold cross-validation with independent test set

https://medium.com/@tzjy/why-is-model-validation-so-important-in-data-science-877fdc70550
 
Model evaluation using sklearn.metrics (MAE — mean absolute error, RMSE — root mean squared error), 
and comparison of observed 
and forecast value integrals (yearly absolute energy demand in MWh)

## Timeseries
https://otexts.com/fpp3/stationarity.html
https://otexts.com/fpp3/tscv.html


https://medium.com/analytics-vidhya/multi-seasonal-time-series-analysis-decomposition-and-forecasting-with-python-609409570007

Multi seasonal time series analysis: decomposition and forecasting with Python
ARIMA models are still frequently used among other modern machine learning and deep learning techniques. Despite its popularity, ARIMA models have some serious drawbacks:
the coefficients of the model are not easy to interpret or need detailed explanation
efficient for small data sets, it is computationally expensive
assumes stationarity of data or else the inputs should be transformed. 
Consequently, forecasts refer to the transformed data and not to the original time series. 
Apart from interpretability, this property increases confidence intervals relative to stationary series without transformation
For a better interpretation of seasonal time series, other methods have been developed such as the Unobserved Components Model (UCM). 
Being a so called ‘state space’ model, UCM decompose the original time series to its individual level, trend, cyclic, seasonal components and predict future values by modeling and taking the sum of these components.
This article is for practical purposes, for more information on state space models and specifically UCM, please follow the underlined links. 
Statsmodels user guide is also available here, but I applied the method to a more illustrative and larger data set.
The goal of the analysis is to forecast energy demand one year ahead using the available past values. Optionally, the model can be refined using exogenous variables. Some such variables were selected, collected and fed to the model.

https://towardsdatascience.com/multi-step-time-series-forecasting-with-arima-lightgbm-and-prophet-cc9e3f95dfb0

We need stationary time series to develop stable linear models, such as ARIMA.
Below we are setting up and executing a function that shows autocorrelation (ACF) and partial autocorrelation (PACF) plots 
along with performing Augmented Dickey–Fuller unit test.

Comparing ThymeBoost, Pmdarima, and Prophet:

https://towardsdatascience.com/auto-forecasting-in-python-with-thymeboost-8bc9bd466998

https://towardsdatascience.com/multi-step-time-series-forecasting-with-arima-lightgbm-and-prophet-cc9e3f95dfb0

### PyCaret
https://github.com/pycaret/pycaret/discussions/1760

https://towardsdatascience.com/announcing-pycarets-new-time-series-module-b6e724d4636c
 

https://medium.com/@mywork.ng/pycaret-time-series-module-architecture-overview-57336a2f39c7

The pycaret time series module is built on top of sktime which is a unified framework for time series analysis. 
sktime https://www.sktime.org/en/stable/tutorials.html
aims to do for time series analysis what sklearn did for machine learning. 
 
sktime provides a framework to:
- Create time series models with sklearn regressors using the reduced regression technique  
- Create models pipelines with transformations akin to what sklearn provides.
- Connect to other time series packages (such as statsmodels, pmdarima, tbats, prophet, etc) using adapters.
- Allow users to create their own forecasting models using extension templates.
