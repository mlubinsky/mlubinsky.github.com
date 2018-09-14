## Kagle

<https://www.kaggle.com/c/demand-forecasting-kernels-only/>

<https://www.kaggle.com/c/demand-forecasting-kernels-only/kernels>

<https://www.kaggle.com/shivamb/data-science-glossary-on-kaggle/notebook>

You are given 5 years of store-item sales data, and asked to predict 3 months of sales for 50 different items at 10 different stores.

What's the best way to deal with seasonality? Should stores be modeled separately, or can you pool them together? Does deep learning work better than ARIMA? Can either beat xgboost?


date - Date of the sale data. There are no holiday effects or store closures.
store - Store ID
item - Item ID
sales - Number of items sold at a particular store on a particular date.

```
cat  train.csv | cut -d "," -f2 | sort | uniq -c
91300 1
91300 10
91300 2
91300 3
91300 4
91300 5
91300 6
91300 7
91300 8
91300 9
```

<https://www.kaggle.com/praymond/eda-of-total-sales>

<https://www.kaggle.com/princeashburton/plotting-time-series-data>

<https://www.kaggle.com/darshanadiga/time-series-data-exploration>

<https://www.kaggle.com/viridisquotient/arima>

<https://www.kaggle.com/adityaecdrid/my-first-time-series-comp-added-prophet>

<https://www.kaggle.com/adityaecdrid/my-first-time-series-comp-added-prophet>
```
Seasonal decomp in statmodels:
#from statsmodels.tsa.seasonal import seasonal_decompose
#import statsmodels.api as sm

decomp_year = sm.tsa.seasonal_decompose(sales_a, model = 'additive', freq = 365) . #Yearly
decomp_year.trend.plot(color = c, ax = ax1)

decomp_additive = sm.tsa.seasonal_decompose(y, model='additive')
decomp_additive.plot()


decomp_multi = sm.tsa.seasonal_decompose(y, model='multiplicative')
decomp_multi.plot();
```
## Time series

<https://otexts.org/fpp2/>   FORECASTING BOOK

<https://news.ycombinator.com/item?id=17950058>


Time series problem is different from a regression problem in following ways:

1) The main difference is that a time series is time dependent. So the basic assumption of a linear regression model that the observations are independent doesn’t hold in this case.
2) Along with an increasing or decreasing trend, most Time Series have some form of seasonality trends,i.e. variations specific to a particular time frame.


 Mean Absolute Percentage Error (MAPE)
 Mean Absolute Error (MAE) is the mean of the absolute values of the errors. 

## LSTM
<https://www.altumintelligence.com/articles/a/Time-Series-Prediction-Using-LSTM-Deep-Neural-Networks>

<http://www.jakob-aungiers.com/articles/a/LSTM-Neural-Network-for-Time-Series-Prediction>

<https://github.com/dafrie/lstm-load-forecasting>

<http://www.uokufa.edu.iq/staff/ehsanali/Tan.pdf>
 
<http://mariofilho.com/create-simple-machine-learning-model-predict-time-series/> 

<http://blog.ethanrosenthal.com/2018/03/22/time-series-for-scikit-learn-people-part2/>
  
<http://mariofilho.com/how-to-predict-multiple-time-series-with-scikit-learn-with-sales-forecasting-example/>

<https://trainings.analyticsvidhya.com/dashboard>  Class: creating time Series Forecast with python

<https://www.youtube.com/watch?v=pl6u8PC_1Ns> 

<https://www.youtube.com/watch?v=9X_4i7zdSY8>

<https://www.youtube.com/watch?v=9X_4i7zdSY8> Deep Learning

<https://www.youtube.com/watch?v=9X_4i7zdSY8>  PyFlux

<https://www.youtube.com/watch?v=VYpAodcdFfA> two Effective Algorithms for Time Series Forecasting

<https://www.youtube.com/watch?v=Fm8zcOMJ-9E> tsfresh

<https://towardsdatascience.com/forecasting-with-python-and-tableau-dd37a218a1e5>

<https://www.analyticsvidhya.com/blog/2018/02/time-series-forecasting-methods/> (Python)

<https://www.digitalocean.com/community/tutorial_series/time-series-visualization-and-forecasting>

<https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/>

<https://machinelearningmastery.com/taxonomy-of-time-series-forecasting-problems/>

<https://machinelearningmastery.com/how-to-develop-a-skilful-time-series-forecasting-model/>

<https://github.com/mlubinsky/mlubinsky.github.com/blob/master/ml/PDF/time_series_forecasting_with_python_mini_course.pdf>

<https://www.kdnuggets.com/2018/09/end-to-end-project-time-series-analysis-forecasting-python.html>
 
<https://blog.algorithmia.com/introduction-to-time-series/>

<https://habrahabr.ru/post/180409/>

<https://habr.com/company/ods/blog/327242/>

<https://medium.com/@ATavgen/time-series-modelling-a9bf4f467687>

<https://waterprogramming.wordpress.com/2017/09/29/time-series-modeling-arma-notation-part-1/>

<https://waterprogramming.wordpress.com/2017/12/18/preparing-data-for-a-time-series-analysis/>

<https://habrahabr.ru/company/ods/blog/327242/>  Time series with python

<http://www.datasciencecentral.com/profiles/blogs/21-great-articles-and-tutorials-on-time-series>
	 



## Anomaly detection 
<https://habrahabr.ru/post/344762/>

<https://blog.statsbot.co/time-series-anomaly-detection-algorithms-1cef5519aef2>

<http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-8/>

<https://en.wikipedia.org/wiki/Anomaly_detection>
