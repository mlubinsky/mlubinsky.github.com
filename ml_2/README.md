https://developers.google.com/machine-learning/crash-course/

Beta distibution

https://medium.com/analytics-vidhya/once-again-beta-distribution-db467a7eded0

https://python.plainenglish.io/matrix-calculation-with-python-5df443c8911f Matrix operations 

https://psrivasin.medium.com/p-value-in-hypothesis-testing-9c071775405d p-value

https://towardsdatascience.com/a-checklist-of-basic-statistics-24b1d671d52

https://benjaminobi.medium.com/mastery-of-data-science-theory-will-make-you-stand-out-e569b1220b1d

### Interview
https://medium.com/geekculture/24-maxims-every-data-scientist-should-know-d9ef9df5887e

https://medium.com/codex/data-science-interview-prep-machine-learning-concepts-1b2f16b584ca

https://medium.com/@tzjy/data-science-interview-prep-supervised-learning-models-3fc2a8f1cd5c

https://medium.com/analytics-vidhya/5-question-series-data-science-ai-4-3070be5632a2

### Heatmap pairplot  Q-Q plot
 Quantile-Quantile plots.   plot the quantiles of a sample distribution against quantiles of a theoretical distribution. Doing this helps us determine if a dataset follows any particular type of probability distribution like normal, uniform, exponential.
https://medium.com/@khandelwal.akansha/q-q-plot-ensure-your-ml-model-is-based-on-the-right-distribution-fe52b6ff4332

https://medium.com/omics-diary/how-to-evaluate-relatedness-between-categorical-variables-using-the-seaborn-library-93f2c00784da

```
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats 
from scipy.stats import pearsonr
pvals = pd.DataFrame([[pearsonr(df_log2FC[c], df_log2FC[y])[1] for y in df_log2FC.columns] for c in df_log2FC.columns],
 columns=df_log2FC.columns, index=df_log2FC.columns)
pvals

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style('white'):
 f, ax = plt.subplots(figsize=(10, 7))
 ax = sns.heatmap(corr, cmap='vlag', mask=mask, center=0, square=True, linewidths=2, annot=True, cbar_kws={'shrink': .5})
 
  = sns.pairplot(df_log2FC)
g.map_lower(sns.regplot)
```

https://medium.com/codex/11-ml-algorithms-you-should-know-in-2021-8fecbd3a2a1a

https://towardsdatascience.com/key-concepts-to-improve-your-understanding-of-probability-theory-ca1d999dd6c9

https://towardsdatascience.com/binomial-distribution-ec76d74952c4  Binomial

https://towardsdatascience.com/change-column-data-type-in-pandas-954d7acdef1d

https://towardsdatascience.com/a-beginners-guide-to-discrete-time-markov-chains-d5be17cf0e12

The Markov property states that p_ij is independent of the state in which the system was at times (t-2), (t-3),…,0. The Markov property is stated as follows:

https://medium.com/pythoneers/30-basic-machine-learning-questions-answered-692acd10841f
```
The Stages of Building A Machine Learning Model 
- Data Collection: It is the first stage of any kind of machine learning model. In this stage, the appropriate data is decided and then it is collected using some algorithm or manually.
- Data Processing: In this stage, the data that we have collected in the first stage is preprocessed by handling all the null values, categorical data, etc. also in the same stage the data features are made in the same range if they are not already.
- Model Building: In this stage first we choose appropriate algorithms to create the model and then with the help of sklearn the model is built.
- Model Evaluation: After the model is created it is evaluated using some techniques of statistics like

Type I and Type II errors 
- Type I Error(False Positive Error):- It occurs when the null hypothesis is true but it gets rejected means if claims something has happened when it hasn’t.
- Type II Error(False Negative Error):-it occurs when the null hypothesis gets accepted when it's not true means it claims nothing when something has happened.

True Positive: Actual Value = Predicted Value when o/p is 1
True Negative : Actual Value != Predicted Value when o/p is 0
False Positive: Type I Error
False Negative: Type II Error

Precision is the ratio of correctly predicted positive observation and total predicted positive observation. It shows how precise our model is.
Precision = TP/TP+FP
Recall is the ratio of the correct predicted positive observation and the total observation in the class.
Recall = TP/TP+FN

F1-Score is the weighted average of recall and precision.
F1-Score = 2*(Recall * Precision) / (Recall + Precision)
Accuracy is the ratio of correctly predicted positive observations to the total positive observations.
Accuracy = TP+TN/TP+TN+FP+FN

P-Value is the determination of a result when the null hypothesis assumed to be true. if the p-value is very small (<0.05) then our assumption that the null hypothesis is correct is most likely to be false. Thus we reject the null hypothesis.

14. Explain how a Roc Curve Works?
Ans: An Roc curve is a graph showing the performance of a classification model at different thresholds. it uses two curve plot parameters True positive rate(sensitivity) and False positive rate(Specificity).
◾ The closer the curve follows the left-hand border and then the top border the more accurate the test is.
◾ The closer the curve to a 45* diagonal of ROC Space the less accurate the test is.

15. How Knn different from K-means clustering?

Ans: Knn is a supervised machine learning technique that is used for classification or regression problems. In Knn the K represents the number of nearest neighbors used to predict the dependent var.
K-means clustering is an unsupervised machine learning algorithm that is used to divide the data into different clusters based on k (number of clustering), and centroids.

16. What is ‘Naive’ in the Naive Bayes Theorem?

Ans: Naive Bayes classifier assumes that all the input variables are independent of each other means they don’t have any relationship between them which is actually an unrealistic assumption for real data.
Let’s suppose a dataset that contains information about fruits and detects whether the fruit is an apple or not. A sample of this data contains a fruit that is red, round, and about 4'' in diameter. Even if all these features depend on each other or upon the existence of the other feature A Naive Bayes classifier will always consider them as independent contributors for the prediction of the fruit.
17. How Ensemble Learning Works?

Ans: Ensemble Learning is a technique in which the predictions or results of multiple models are combines to achieve better performance. Let’s Take an example if you buy a car you generally go for research on the web to search for reviews and features of different cars and In the end, after combining all the reviews you create your own review of that car and decide whether you want to purchase or not. The review you create is the better version of all the reviews you read because it contains the information from all the reviews. 
Ensemble learning works the same, The predictions from many algorithms are used to create a better model.
Ensemble Learning can be done using two ways, one is to use different algorithms prediction combine to generate a new high accuracy prediction or another way is to use a single algorithm multiple times and at the end, use each model prediction to generate a better model with good accuracy.
“Don’t Let Yesterday Take Up Too Much Of Today.” — Will Rogers

18. What is bagging and Boosting in machine learning?

Ans: Bagging is a method of combining predictions of the same type means from the same algorithm. Ex: Random Forest. In this, each model is built independently with equal weight given to them. It reduces the overfitting problem. it also decreases the variance.
Boosting is a way of combining predictions belongs to different algorithms. Ex: Gradient boosting. The new model is highly influenced by the performance of the previously built models. It reduces the bias.

19. What is a bias-variance tradeoff?

Ans: bias is the difference between the average prediction of the model and the correct value on the other hand variance is the variability of a data point that shows the spread of the data.
if our model has fewer parameters then it may have High bias and Low variance because of that it will consistent but inaccurate on average.
A model with a large number of parameters may have Low bias and High variance models which are mostly accurate on average but inconsistent in nature.
A good model always has low bias and low variance.

20. Explain L1 and L2 Regularization?

Ans: A Regression model that uses L1 Regularization is called Lasso Regression and the Model which uses L2 Regularization is called Ridge Regression. 
◾ L1 regularization adds the penalty term in the cost function by adding the absolute value of weight(Wj), while L2 regularization adds the squared value of weights(Wj) in the cost function.
◾ One More difference between both of them is that L1 regularization tries to estimate the median of the data while L2 regularization tries to estimate the mean of the data. 
◾ L1 regularization helps in eliminating the features that are not important.

21. What are the different ways you know to handle missing values in machine learning?

Ans: 1. Replacing the missing value with the mean, median, or mode.
2. Replacing the missing values with a random value.
3. Taking all the NaN values and using them as a New Feature.
4. Replacing NaN values with the third deviation value.
5. Replacing NaN with Lease or Last Outlier
6. Replacing NaN with the most frequent Category (Categorical Values)
7. Treating the missing values as a new category
8. Apply a classifier to predict NaN values
9. Drop Values


Handle Categorical Values in the dataset?

Ans: To Handle Categorical Values We Can Perform Encoding That Basically converts the categorical data into numerical data.

Nomial Encoding: When data do not have an inherent order.
1.1 One Hot Encoding
1.2 One Hot Encoding with many features
1.3 Mean Encoding

Ordinal Encoding: When data have an inherent order.
2.1 Label Encoding
2.2 Target Guided Encoding

3. Count Encoding


```

bayes: https://towardsdatascience.com/bayes-theorem-the-core-of-machine-learning-69f5703e511f

central limit theorem (the sampling distribution of the sample means will be approximately normal distribution even if the original distribution wasn’t normally distributed)

https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/

https://chetna-shahi31.medium.com/hypothesis-testing-bae1e74543f


https://medium.com/analytics-vidhya/why-should-your-company-do-an-ab-testing-88d42ec8337c

###  2-sided hypotesis : there are 2 types of Hypothesis:
```
1. Null Hypothesis: Previous value and observed values from the claim are same.
Null Hypothesis treats everything same or equal.
Null hypothesis states that there is no relationship between the two variables being studied (one variable does not affect the other). 
It states the results are due to chance and are not significant in terms of supporting the idea being investigated. 
Thus, the null hypothesis assumes that whatever you are trying to prove did not happen.

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

```
corrMatrix = df.cor()
import seaborn as sn
sn.heatmap(corrMatrix, annot=True)
```

Types of Correlation coefficients:  https://towardsdatascience.com/beyond-correlation-coefficients-and-mean-squared-error-952bd966cedb

1. Sample Correlation coefficients.
2. Population Correlation coefficients.
3. Pearson Correlation coefficients.

 Predictive Power Score PPS can uncover non-linear relationships between different columns and data types (non-numeric), is asymmetric and will show values, for example, if variable A can predict B and values for variable B to predict A.
https://medium.com/geekculture/an-alternative-to-correlation-predictive-power-score-in-python-a3160c95d701

autoviz and lux
https://bobrupakroy.medium.com/autoviz-and-lux-8de6fe4d9a25
sweetviz
https://bobrupakroy.medium.com/sweetviz-one-liner-eda-b4c645612845 
mito
https://towardsdatascience.com/mito-speed-up-dataset-manipulation-with-no-coding-407b8c72f46f 

### Apriori Algo
https://medium.com/analytics-vidhya/apriori-algorithm-a1f8589f32a0 

### Logistic regression

https://towardsdatascience.com/logistic-regression-from-first-principles-in-python-82f238effef1

### Linear Regression
https://medium.com/@amitjain2110/10-assumptions-of-linear-regression-c58f8703d657

Linear Regression is a model used to fit a line or hyperplane to a dataset where the output is continuous and has residuals which are normally distributed. 

Imagine you are a phone operator and want to predict how many calls you will receive in a day. Do you think Linear Regression would be a suitable model? 
The answer is NO for the following reasons:
The number of calls have to be greater or equal to 0, whereas in Linear Regression the output can be negative as well as positive.

The Poisson distribution is a probability distribution that measures how many times and how likely x (calls) will occur over a specified period. 

https://towardsdatascience.com/complete-guide-to-regressional-analysis-using-python-bbe76b3e451f
```
In Machine Learning, tasks are often split into four major categories: Supervised Learning, Unsupervised Learning, Semi-Supervised Learning, and Reinforcement Learning.
Regression falls into the domain of Supervised Learning, where the goal is to learn or model a function that maps a set of inputs to a set of outputs.
In Supervised Learning, our set of outputs are commonly called the dependent variable in statistics or the target variable in the Machine Learning Community. This target variable can either be discrete, commonly called Classification, or continuous, commonly called Regression.
In this way, Regression is simply trying to predict a continuous target variable given a set of inputs
```

Generalised Linear Models - GLM
https://towardsdatascience.com/what-is-so-general-about-generalized-linear-model-15dde9be2640

GLM’s are a generalisation of Linear Regression where the response variable takes a non-normal distribution such as a Poisson or Binomial distribution. GLM’s contain three core things:
- Part of the Exponential Family of Distributions
- Linear Predictors
- Link Function
 
https://towardsdatascience.com/poisson-regression-and-generalised-linear-models-606fe5f7c1fd


### Streaming Algo
https://towardsdatascience.com/introduction-to-streaming-algorithms-b71808de6d29
 algorithms that are able to process an extremely large, maybe even unbounded, data set and compute some desired output using only a constant amount of RAM.

```
class StreamingMean:
    def __init__(self):
        self.result = 0
        self.n = 0

    def update(self, element):
        self.result = (self.result * self.n + element) / (self.n+1)
        self.n += 1
```
https://en.wikipedia.org/wiki/Reservoir_sampling
```
from random import random

class ReservoirSampler:
    def __init__(self):
        self.result = None
        self.n = 0

    def update(self, element):
        self.n += 1
        if random() < 1 / self.n:  # Satisfied with prob. 1/n.
            self.result = element
```
### Clustering

https://medium.com/analytics-vidhya/a-cheatsheet-to-clustering-algorithms-a2d49fa2cc69

https://medium.com/analytics-vidhya/less-known-applications-of-k-means-clustering-dimensionality-reduction-anomaly-detection-and-908f4bee155f

https://medium.com/softplus-publication/clustering-harness-the-power-of-kmeans-and-gmm-using-sklearn-2b9e2aea61dd

### Sampling

https://medium.com/@tzjy/4-typical-sampling-methods-you-need-for-data-science-jobs-python-code-included-b003feb6504b


### Transformation /scaling /normalization

https://medium.com/@tzjy/feature-scaling-and-normalization-do-they-matter-to-machine-learning-algorithm-ebbb07dd3efc

to normal dist

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

https://medium.com/low-code-for-advanced-data-science/anomaly-detection-for-predictive-maintenance-exploratory-data-analysis-56d13f1bc212

https://medium.com/low-code-for-advanced-data-science/anomaly-detection-for-predictive-maintenance-control-charts-abcbe656c2d0

Isolation forest is an unsupervised learning algorithm that works on the principle of isolating anomalies. 
Isolation Forest like any other tree ensemble method is built on the basis of the decision tree. Just a Random Forest here in Isolation Forest we are isolating the extreme values.
Extreme values are less frequent than regular observations i.e. they lie further from the regular observations in the feature space. 
Thus with random sub-sampling/bootstrap aggregating like in the random forest, isolation forest is able to identify and isolate the extreme values.
https://bobrupakroy.medium.com/isolation-forest-7aa9bb9825cf

###  Local Outlier Factor - LOF
https://bobrupakroy.medium.com/local-outlier-factor-lof-5d358ef8fd06
https://arshren.medium.com/anomaly-detection-using-local-outlier-factor-4e52f16894f


### Feature selection

https://pub.towardsai.net/feature-selection-and-removing-in-machine-learning-dd3726f5865c

https://bechirtr97.medium.com/feature-selection-in-unsupervised-learning-problems-585a56d024bd

In the case of supervised learning, this task is relatively easy thanks to preexisting tricks, 
such as feature importance embedded in many scikit learn models perse 
(i.e Random Forrests, linear regression, logistic regression …etc.),
and the existence of loss functions computable directly is also a big help, 
as we can always run an exhaustive search with a fixed model and compare the obtain loss scores.

https://towardsdatascience.com/how-to-mitigate-overfitting-with-feature-selection-164897c0c3db

Following techniques that can be used to mitigate overfitting:
Cross-validation
Regularization
Dimensionality Reduction
Creating Ensembles
Feature Selection


### Model evaluation

https://medium.com/@amitjain2110/important-model-evaluation-error-metrics-b649bca8ea74
 
1. RMSE: Root Mean Squared Error
2. ME: Mean Error
3. MAE: Mean Absolute Error
4. MAPE: Mean Absolute Percentage Error
5. MASE: Mean Absolute Scaled Error
6. Confusion Matrix
7. Gain and Lift Chart
8. Kolmogorov Smirnov Chart
9. AUC — ROC
10. Gini Coefficient
11. Concordant — Discordant…

 Regression: regression is a process of finding the correlation between the dependent and independent variables. it is helpful in the prediction of the continuous variables such as the prediction of Stock Market, House prices, etc. 
 In regression, our task is to find the best suitable line that can predict the output accurately.

Classification: Classification is the process of finding a function that helps in dividing the data into different classes. These are mainly used in discrete data. 
In Classification, our aim is to find the decision boundary which can divide the dataset into different classes.


https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9

Confusion Matrices are the most basic way of interpreting a Classification Model. 
They hold four important values which describe the results of a Classification Model:
True Positives(TP), False Positives(FP), False Negatives(FN) and True Negatives(TN). 
When we plot a Confusion Matrix we would like the values on the main diagonal (TP and TN)
to be as large as possible.

https://medium.com/softplus-publication/machine-learning-model-evaluation-and-interpretation-with-python-977ea324842

https://www.dataquest.io/blog/understanding-regression-error-metrics/

https://towardsdatascience.com/beyond-correlation-coefficients-and-mean-squared-error-952bd966cedb

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
RMSE — root mean squared error  is the square root of the average of squared residuals  

and comparison of observed 
and forecast value integrals (yearly absolute energy demand in MWh)


### PCA

 PCA uses some techniques to find the most important features or directions in the data and then it can discard unimportant parts to get the desired dimensionality of the target space.
 
 https://medium.com/mlearning-ai/principal-component-analysis-explained-with-example-e1c4890ef420
 
## Timeseries

Book
https://otexts.com/fpp3/stationarity.html
https://otexts.com/fpp3/tscv.html

#### Change point detection
https://medium.com/@baw_H1/bayesian-approach-to-time-series-change-point-detection-613bf9376568

 A change-point (CP) is abstraction for an abrupt change in a TS; its value is the time-index at which the TS changes its behavior. The behavior of a TS before the CP is different from that after the CP. More specifically, a CP is a point in time at which the parameters of the underlying distribution or the parameters of the model used to describe the TS abruptly change (e.g. mean, variance, trend) ([1]). This characterization underlies the proposed method discussed below. CP detection is about the statistical characterization of a CP. 
 
ARIMA
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
