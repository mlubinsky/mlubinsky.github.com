https://developers.google.com/machine-learning/crash-course/

https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/

https://chetna-shahi31.medium.com/hypothesis-testing-bae1e74543f

There are 2 types of Hypothesis:
```
Null Hypothesis: Previous value and observed values from the claim are same.
Null Hypothesis treats everything same or equal. Null hypothesis states that there is no relationship between the two variables being studied (one variable does not affect the other). It states the results are due to chance and are not significant in terms of supporting the idea being investigated. Thus, the null hypothesis assumes that whatever you are trying to prove did not happen.
2. Alternative Hypothesis: Mathematically opposite of Null hypothesis.
Hypothesis Type is determined based on Test (Statistics):

Chi-squared Test : A chi-square test requires categorical variables, usually only two, but each may have any number of levels.

t-student Test : A t-test requires two variables; one must be categorical and have exactly two levels, and the other must be quantitative and be estimable by a mean. For example, the two groups could be Republicans and Democrats, and the quantitative variable could be age.

Fisher’s Z Test: In a z-test, the sample is assumed to be normally distributed.

ANOVA Test: It is also called an analysis of variance and is used to compare multiple (three or more) samples with a single test. It is used when the categorical feature has more than two categories.


After the test results, you can use Level of Significance to determine if Null hypothesis would be accepted or rejected.
Level of Significance (alpha): Shows amount of data that is significant. It can be either 5% or 1%. Shows if there ≤5% gap between observed and previous value then the null hypothesis is accepted.

Level of Confidence ( c ): Shows confidence in data. It will be 95% if alpha is 5%
alpha + c = 1
p-value is probability of Null Hypothesis to be true. If its <0.05 then we reject Null Hypothesis.
```
### Plotting
Seaborn pairplot   (pair-wise scatter plot(
Heatmap
Cross-correlation plot

autoviz and lux
https://bobrupakroy.medium.com/autoviz-and-lux-8de6fe4d9a25
sweetviz
https://bobrupakroy.medium.com/sweetviz-one-liner-eda-b4c645612845 
mito
https://towardsdatascience.com/mito-speed-up-dataset-manipulation-with-no-coding-407b8c72f46f 

### Regression
Linear Regression is a model used to fit a line or hyperplane to a dataset where the output is continuous and has residuals which are normally distributed. 

Imagine you are a phone operator and want to predict how many calls you will receive in a day. Do you think Linear Regression would be a suitable model? 
The answer is NO for the following reasons:
The number of calls have to be greater or equal to 0, whereas in Linear Regression the output can be negative as well as positive.

The Poisson distribution is a probability distribution that measures how many times and how likely x (calls) will occur over a specified period. 

Generalised Linear Models GLM

GLM’s are a generalisation of Linear Regression where the response variable takes a non-normal distribution such as a Poisson or Binomial distribution. GLM’s contain three core things:
- Part of the Exponential Family of Distributions
- Linear Predictors
- Link Function
 
https://towardsdatascience.com/poisson-regression-and-generalised-linear-models-606fe5f7c1fd

### Clustering

https://medium.com/softplus-publication/clustering-harness-the-power-of-kmeans-and-gmm-using-sklearn-2b9e2aea61dd

### Sampling

https://medium.com/@tzjy/4-typical-sampling-methods-you-need-for-data-science-jobs-python-code-included-b003feb6504b


### Transformation to normal dist

https://medium.com/softplus-publication/bring-your-data-to-normal-distribution-with-imperio-yeojohnsontransformer-f4bb09402e1e

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


## Anomaly detection
Isolation forest is an unsupervised learning algorithm that works on the principle of isolating anomalies. 
Isolation Forest like any other tree ensemble method is built on the basis of the decision tree. Just a Random Forest here in Isolation Forest we are isolating the extreme values.
Extreme values are less frequent than regular observations i.e. they lie further from the regular observations in the feature space. 
Thus with random sub-sampling/bootstrap aggregating like in the random forest, isolation forest is able to identify and isolate the extreme values.
https://bobrupakroy.medium.com/isolation-forest-7aa9bb9825cf

###  Local Outlier Factor - LOF
https://bobrupakroy.medium.com/local-outlier-factor-lof-5d358ef8fd06
https://arshren.medium.com/anomaly-detection-using-local-outlier-factor-4e52f16894f


### Feature selection

https://towardsdatascience.com/how-to-mitigate-overfitting-with-feature-selection-164897c0c3db

 following techniques that can be used to mitigate overfitting:
Cross-validation
Regularization
Dimensionality Reduction
Creating Ensembles
Feature Selection


### Model evaluation

https://towardsdatascience.com/4-metrics-to-evaluate-your-regression-models-885e9caeee57

https://arxiv.org/abs/1811.12808
Sebastian Raschka gave a very nice summary in his paper, Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning, of 4 model validation methods:
Performance estimation
- 2-way holdout method (train/test split)
- (Repeated) k-fold cross-validation without independent test set
- Model selection (hyperparameter optimization) and performance estimation
- 3-way holdout method (train/validation/test split)
- (Repeated) k-fold cross-validation with independent test set

https://medium.com/@tzjy/why-is-model-validation-so-important-in-data-science-877fdc70550
 
 
https://towardsdatascience.com/4-metrics-to-evaluate-your-regression-models-885e9caeee57 
Model evaluation using sklearn.metrics
MSE - Mean Squared Error  the MSE penalizes large errors.
MAPE  - Mean Absolute Percentage Error 
MAE — mean absolute error, 
RMSE — root mean squared error), 
and comparison of observed 
and forecast value integrals (yearly absolute energy demand in MWh)


### PCA

 PCA uses some techniques to find the most important features or directions in the data and then it can discard unimportant parts to get the desired dimensionality of the target space.
 
 https://medium.com/mlearning-ai/principal-component-analysis-explained-with-example-e1c4890ef420
 
## Timeseries

Book
https://otexts.com/fpp3/stationarity.html
https://otexts.com/fpp3/tscv.html


https://medium.com/@appravi18/time-series-analysis-with-classic-statistical-methods-fe6dfaf0cd4a

Kaggle
https://towardsdatascience.com/key-takeaways-from-kaggles-most-recent-time-series-competition-ventilator-pressure-prediction-7a1d2e4e0131

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
