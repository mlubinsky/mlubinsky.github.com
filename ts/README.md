https://mlcourse.ai/articles/topic9-part1-time-series/

https://towardsdatascience.com/breakthroughs-in-time-series-forecasting-at-neurips-2020-1dc1b9b6d99d

## packtpub

https://subscription.packtpub.com/book/big-data-and-business-intelligence/9781788290227

https://subscription.packtpub.com/video/data/9781838640590

## coursera

https://www.coursera.org/learn/practical-time-series-analysis

### Youtube

https://www.youtube.com/watch?v=-r7wB9DJtiU&list=PL3N9eeOlCrP5cK0QRQxeJd6GrQvhAtpBK

### Time series packages in Python

https://www.microprediction.com/blog/popular-timeseries-packages

https://github.com/MaxBenChrist/awesome_time_series_in_python


How to Build Exponential Smoothing Models Using Python: Simple Exponential Smoothing, Holt, and Holt-Winters

https://medium.com/datadriveninvestor/how-to-build-exponential-smoothing-models-using-python-simple-exponential-smoothing-holt-and-da371189e1a1


https://rubikscode.net/2020/11/15/top-9-feature-engineering-techniques/

 
https://youtu.be/_fwhJvPW32g Time series Cross Validation

### Features based on time:
https://www.kaggle.com/kashnitsky/correct-time-aware-cross-validation-scheme
```
def add_time_features(df, X_sparse):
    hour = df['time1'].apply(lambda ts: ts.hour)
    morning = ((hour >= 7) & (hour <= 11)).astype('int')
    day = ((hour >= 12) & (hour <= 18)).astype('int')
    evening = ((hour >= 19) & (hour <= 23)).astype('int')
    night = ((hour >= 0) & (hour <= 6)).astype('int')
    X = hstack([X_sparse, morning.values.reshape(-1, 1), 
                day.values.reshape(-1, 1), evening.values.reshape(-1, 1), 
                night.values.reshape(-1, 1)])
    return X
 ```   
 
## mljar-supervised

https://github.com/mljar/mljar-supervised


### PyTorch-forecasting
pip install pytorch-forecasting

https://pytorch-forecasting.readthedocs.io/en/latest/

https://github.com/jdb78/pytorch-forecasting

### Flow-forecast

Deep learning PyTorch library for time series forecasting, classification, and anomaly detection (originally for flood forecasting).

https://github.com/AIStream-Peelout/flow-forecast
 
### Auto_TS

https://github.com/AutoViML/Auto_TS

### AutoTS

https://github.com/winedarksea/AutoTS

## pycaret

https://pycaret.org/

https://www.analyticsvidhya.com/blog/2020/05/pycaret-machine-learning-model-seconds/

Anomaly detection :

https://github.com/pycaret/pycaret/blob/master/tutorials/Anomaly%20Detection%20Tutorial%20Level%20Beginner%20-%20ANO101.ipynb


## darts  

pip install 'u8darts[all]'

https://medium.com/unit8-machine-learning-publication/darts-time-series-made-easy-in-python-5ac2947a8878

https://github.com/unit8co/darts

## Stumpy

conda install stumpy

https://stumpy.readthedocs.io/en/latest/index.html

https://www.youtube.com/watch?v=xLbPP5xNIJs

https://notamonadtutorial.com/stumpy-unleashing-the-power-of-the-matrix-profile-for-time-series-analysis-7c46af040adb

### sktime and sktime-dl

<https://habr.com/ru/company/otus/blog/511782/>. sktime - time series with python

https://github.com/alan-turing-institute/sktime  SkTime - time series analysis

https://news.ycombinator.com/item?id=24541487 . SkTime - time series analysis

https://github.com/alan-turing-institute/sktime/blob/master/examples/01_forecasting.ipynb

pip install sktime-dl

https://github.com/sktime/sktime-dl

### XBoost LightGBM 
```
pip list | grep xgboost
xgboost                            1.31

(mljar) virtualenv

pip list | grep xgboost
xgboost            1.2.0
```
https://medium.com/@qs2178/time-series-forecasting-with-stacked-machine-learning-models-7250abdece0f

https://github.com/atriptoparadise/Time-Series-with-machine-learning/blob/master/Time%20Series%20Forecasting%20with%20Stacked%20Machine%20Learning%20Models_DEMO.ipynb


### Links

https://www.cs.ucr.edu/~eamonn/100_Time_Series_Data_Mining_Questions__with_Answers.pdf

<https://spark-in.me/post/playing-with-electricity> Good links!

https://github.com/SeldonIO/alibi-detect

https://github.com/axsaucedo/seldon_experiments/blob/master/monitoring-talk/cifar10_example.ipynb


https://youtu.be/6OGSftP2_Ts



<https://zerowithdot.com/time-forecasting-challenges/>


<https://habr.com/ru/post/180409/> Обзор моделей прогнозирования временных рядов

<https://habr.com/ru/post/207160/> . statmodels

<https://habr.com/ru/post/436294/>


<https://habr.com/ru/company/ods/blog/327242/> Открытый курс машинного обучения. Тема 9. Анализ временных рядов с помощью Python

<https://www.vaishalilambe.com/blog/learning-time-series-analysis-forecasting-phase-1>



<https://machinelearningmastery.com/taxonomy-of-time-series-forecasting-problems/>

<https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/>



## NN for time series
<https://habr.com/ru/post/495884/> NN for time series

<https://vorstella.com/deep-learning-time-series/>

<https://medium.com/tensorflow/structural-time-series-modeling-in-tensorflow-probability-344edac24083>

<https://www.m3db.io/> Uber's TS database

<https://www.dataengineeringpodcast.com/datadog-timeseries-data-episode-113/>



### packages

<https://medium.com/@michalchromcak/hcrystalball-a-unified-interface-to-time-series-forecasting-6fb57384ad57> 

<https://github.com/firmai/atspy> Automated Time Series Models in Python (AtsPy)
```
ARIMA - Automated ARIMA Modelling
Prophet - Modeling Multiple Seasonality With Linear or Non-linear Growth
HWAAS - Exponential Smoothing With Additive Trend and Additive Seasonality
HWAMS - Exponential Smoothing with Additive Trend and Multiplicative Seasonality
NBEATS - Neural basis expansion analysis (now fixed at 20 Epochs)
Gluonts - RNN-based Model (now fixed at 20 Epochs)
TATS - Seasonal and Trend no Box Cox
TBAT - Trend and Box Cox
TBATS1 - Trend, Seasonal (one), and Box Cox
TBATP1 - TBATS1 but Seasonal Inference is Hardcoded by Periodicity
TBATS2 - TBATS1 With Two Seasonal Periods
```

<https://news.ycombinator.com/item?id=23041264> ts models

<https://arxiv.org/abs/1911.13288> finansial TS with deep learning

## Time Series DBs

<https://medium.com/datadriveninvestor/what-are-time-series-databases-a3e847608f91>

<https://questdb.io/blog/>

<https://news.ycombinator.com/item?id=23975807>

<https://github.com/timescale/tsbs> Benchmarking

<https://habr.com/ru/post/508362/> VictoriaMetrics, TimescaleDB и InfluxDB

<https://www.youtube.com/watch?v=2SUBRE6wGiA&list=PLSE8ODhjZXjY0GMWN4X8FIkYNfiu8_Wl9>

<https://github.com/questdb/questdb>

<https://news.ycombinator.com/item?id=20760324> 

<https://blog.twitter.com/engineering/en_us/topics/infrastructure/2019/metricsdb.html>

<https://habr.com/ru/company/itsumma/blog/462111/>

<https://github.com/richardartoul/tsdb-layer>

<https://github.com/m3db/m3>

<http://rcardin.github.io/database/mongodb/time-series/2017/01/31/implementing-time-series-in-mongodb.html> 

## Time Series

<https://www.amazon.com/Practical-Time-Analysis-Prediction-Statistics-ebook/dp/B07Y5WSCV2/> Book

<https://www.liip.ch/en/blog/time-series-prediction-a-short-comparison-of-best-practices>

<https://news.ycombinator.com/item?id=21492394>

<https://christian.bock.ml/posts/significant_shapelets/> 



<https://www.reddit.com/r/datascience/comments/deiowd/are_there_any_python_libraries_that_help_with/>

<https://machinelearningmastery.com/time-series-data-visualization-with-python/>

<https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b>

<http://www.timeseriesclassification.com/>

<https://tslearn.readthedocs.io/en/latest/index.html> .  tslearn

<https://pyts.readthedocs.io/en/latest/> . pyts

<https://github.com/unit8co/darts> time series in Python


<https://github.com/mlubinsky/mlubinsky.github.com/blob/master/ts/time_series_forecasting_with_python_mini_course.pdf>

<https://habr.com/ru/post/352980/> . Alert system for metrics

<https://www.youtube.com/watch?v=AtS7Fo60JiY> . A Practical Guide to Monitoring and Alerting with Time Series at Scale - Google - SRECon2017

<http://iconcs.org/papers/Paper_95.pdf> .  Big Data Analytics for Load Forecasting in Smart Grids: A Survey

<https://en.wikipedia.org/wiki/Dickey%E2%80%93Fuller_test> . Dickey–Fuller test

## Dataset
<http://traces.cs.umass.edu/index.php/Smart/Smart> . UMass Trace Repository

<https://www.kaggle.com/robikscube/hourly-energy-consumption>

<https://www.kaggle.com/robikscube/hourly-energy-consumption/kernels>

## Prophet (from FaceBook)

https://medium.com/@michalchromcak/hcrystalball-a-unified-interface-to-time-series-forecasting-6fb57384ad57

<https://www.kaggle.com/adityaecdrid/my-first-time-series-comp-added-prophet>

<https://www.kaggle.com/robikscube/tutorial-time-series-forecasting-with-prophet>

## XGBoost
<https://www.kaggle.com/robikscube/tutorial-time-series-forecasting-with-xgboost>

## ARIMA 
<https://ru.wikipedia.org/wiki/ARIMA>

<https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python>

<http://people.duke.edu/~rnau/411arim.htm>

<https://otexts.com/fpp2/arima.html>

<https://www.sas.upenn.edu/~fdiebold/Textbooks.html>


```
Non-seasonal ARIMA has three input values to help control for smoothing, stationarity, and forecasting ARIMA(p,d,q), where:

p is the number of autoregressive terms,
d is the number of nonseasonal differences needed for stationarity, and
q is the number of lagged forecast errors in the prediction equation.

By contrast seasonal ARIMA has six input values ARIMA(p,d,q,P,D,Q), where:

P is the number of seasonal autoregressive terms,
D is the number of seasonal differences, and
Q is the number of seasonal moving-average terms.
```


```
Step 0: Visualization
We can use   resampling by week or month or year available in pandas:
sales_a.resample('W').sum().plot(color = c, ax = ax1)

Step1: split data in 3 sets:  train (biggest), test, and validation

Step2: seasonality check - decompose time series into three components: trend, seasonality, and noise.

import statsmodels.api as sm
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
decomposition.plot();

decomposition = sm.tsa.seasonal_decompose(y, model='multiplicative')

```


<https://machinelearningmastery.com/make-manual-predictions-arima-models-python/>

<https://machinelearningmastery.com/make-sample-forecasts-arima-python/>

<https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/>


<https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3>

<https://www.8host.com/blog/prognozirovanie-vremennyx-ryadov-s-pomoshhyu-arima-v-python-3/>

## Article with code
<https://habr.com/ru/company/ods/blog/327242/>  Анализ временных рядов с помощью Python

<https://github.com/Yorko/mlcourse.ai/blob/master/jupyter_russian/topic09_time_series/topic9_part2_arima_time_series_deaths.ipynb>

## Article with code
<https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/>

<https://github.com/aarshayj/Analytics_Vidhya/blob/master/Articles/Time_Series_Analysis/Time_Series_AirPassenger.ipynb>

## Article with code: Seasonal ARIMA
<https://medium.com/@josemarcialportilla/using-python-and-auto-arima-to-forecast-seasonal-time-series-90877adff03c>
<https://github.com/Pierian-Data/AutoArima-Time-Series-Blog>




<https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/>

<https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/>

<https://www.kaggle.com/viridisquotient/arima>



<https://www.kaggle.com/ctlente/time-series-forecasting-workflow>

<https://ubereng.wpengine.com/forecasting-introduction/>

<https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/>

<https://www.reddit.com/r/MachineLearning/comments/amj60h/d_what_are_some_modern_machine_learning/>

<https://www.reddit.com/r/MachineLearning/comments/9ofd7x/d_machine_learning_on_time_series_data/>

<http://www.uokufa.edu.iq/staff/ehsanali/Tan.pdf>  BOOK Introduction to DataMining

<https://habr.com/company/ods/blog/327242/>

<https://www.youtube.com/watch?v=JNfxr4BQrLk>

## Javascript for Time Series
https://www.quora.com/What-are-the-best-JavaScript-libraries-for-time-series-graphs

## Time series in scikit-learn
<https://www.ethanrosenthal.com/2018/01/28/time-series-for-scikit-learn-people-part1/>
<https://www.ethanrosenthal.com/2018/03/22/time-series-for-scikit-learn-people-part2/>
<https://www.ethanrosenthal.com/2019/02/18/time-series-for-scikit-learn-people-part3/>

<http://mariofilho.com/how-to-predict-multiple-time-series-with-scikit-learn-with-sales-forecasting-example/>

## LSTM
<https://www.altumintelligence.com/articles/a/Time-Series-Prediction-Using-LSTM-Deep-Neural-Networks>

<http://www.jakob-aungiers.com/articles/a/LSTM-Neural-Network-for-Time-Series-Prediction>

<https://github.com/dafrie/lstm-load-forecasting>

## ARIMA vs LSTM 

<https://www.quora.com/When-should-I-use-an-RNN-LSTM-and-when-to-use-ARIMA-for-a-time-series-forecasting-problem-What-is-the-relation-between-them>

<https://arxiv.org/pdf/1803.06386.pdf>

<https://forecasters.org/wp-content/uploads/gravity_forms/7-c6dd08fee7f0065037affb5b74fec20a/2017/07/Laptev_Nikolay_ISF2017.pdf>

<https://www.kaggle.com/kapilstp84/time-series-forecasting-arima-v-s-lstm-rnn>  

<https://springml.com/2018/01/26/time-series-forecasting-arima-vs-lstm/>

<https://www.linkedin.com/pulse/comparison-between-classical-statistical-model-arima-deep-virmani/>

<http://rstudio-pubs-static.s3.amazonaws.com/316135_c44aa19b592a421d97330f03c7965558.html#/>

<https://machinelearningmastery.com/start-here/#timeseries>

<https://machinelearningmastery.com/suitability-long-short-term-memory-networks-time-series-forecasting/>

<https://www.youtube.com/watch?v=H8t8Y_OvB2I&list=PL51yKFtVfMeCI5OVzqToxFoDfIsYfCS-r&t=0s&index=15>

<https://www.youtube.com/watch?v=h9QWefYBfJg>




<https://datascience.stackexchange.com/questions/12721/time-series-prediction-using-arima-vs-lstm>

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

<https://uzclip.net/video/RdTxLXmbvjY/008-%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D1%85-%D1%80%D1%8F%D0%B4%D0%BE%D0%B2-%D0%BA-%D0%B2-%D0%B2%D0%BE%D1%80%D0%BE%D0%BD%D1%86%D0%BE%D0%B2.html>  

<https://uzclip.net/video/kdGsAZfLgFI/%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D0%BE%D1%86%D0%B5%D0%BD%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-arma-%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%B0.html>

<https://www.kaggle.com/kanncaa1/time-series-prediction-tutorial-with-eda>

<https://www.kaggle.com/thebrownviking20/everything-you-can-do-with-a-time-series>

```
Time series problem is different from a regression problem in following ways:

1) The main difference is that a time series is time dependent. So the basic assumption of a linear regression model that the observations are independent doesn’t hold in this case.
2) Along with an increasing or decreasing trend, most Time Series have some form of seasonality trends,i.e. variations specific to a particular time frame.


Stationarity of a Time Series
There are three basic criterion for a time series to understand whether it is stationary series or not.

- constant mean
- constant variance
- autocovariance that does not depend on time. autocovariance is covariance between time series and lagged time series.


 Mean Absolute Percentage Error (MAPE)
 Mean Absolute Error (MAE) is the mean of the absolute values of the errors. 
```

 
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


<http://www.datasciencecentral.com/profiles/blogs/21-great-articles-and-tutorials-on-time-series>
	  
