## A/B testing

<https://habr.com/ru/company/yandex/blog/476826/>

## Anomaly detection

https://www.anodot.com/blog/quick-guide-different-types-outliers/

https://github.com/cerlymarco/tsmoothie

An anomaly detection algorithm should either label each time point with anomaly/not anomaly, 
or forecast a signal for some point and test if this point value varies from the forecasted enough to deem it as an anomaly.

https://blog.floydhub.com/introduction-to-anomaly-detection-in-python/

https://www.datasciencecentral.com/profiles/blogs/anamoly-outlier-detection-using-local-outlier-factors

https://machinelearnings.co/data-science-tricks-simple-anomaly-detection-for-metrics-with-a-weekly-pattern-2e236970d77#.43mcl6cv5
The system should be quite robust and automatically adapt to new baselines.

https://blogs.oracle.com/datascience/introduction-to-anomaly-detection

https://blogs.oracle.com/meena/anomaly-detection

https://blogs.oracle.com/r/early-detection-of-process-anomalies-with-sprt

MERLIN: Parameter-Free Discovery of Arbitrary Length
Anomalies in Massive Time Series Archives:
https://www.cs.ucr.edu/~eamonn/MERLIN_Long_version_for_website.pdf

<https://spark-in.me/post/playing-with-electricity> has good links!

https://arxiv.org/abs/2009.13807

https://towardsdatascience.com/anomaly-detection-with-extreme-value-analysis-b11ad19b601f

### SQL for anomaly detection

https://hakibenita.com/sql-anomaly-detection 

<https://towardsdatascience.com/anomaly-detection-with-sql-7700c7516d1d> Anomality detection with SQL

https://news.ycombinator.com/item?id=25731699

<https://nickgavalas.com/anomaly-detection-on-data-streams-in-one-line-of-bash/>

https://habr.com/ru/post/530574/ .  Deep Anomaly Detection

<https://pyod.readthedocs.io/en/latest/> . outliers detection

<https://habr.com/ru/post/477450/>



<https://en.wikipedia.org/wiki/Anomaly_detection>

<https://blog.floydhub.com/introduction-to-anomaly-detection-in-python/> Python

<https://github.com/arundo/adtk> Python

<https://blog.statsbot.co/time-series-anomaly-detection-algorithms-1cef5519aef2>

<https://www.datascience.com/blog/python-anomaly-detection>

<http://www.vldb.org/pvldb/vol10/p1358-rong.pdf>

<https://github.com/MateLabs/AutoOut> Outlier detection

<https://habrahabr.ru/post/344762/>

<https://www.youtube.com/watch?v=9EYmmOz1db0>

<https://blog.statsbot.co/time-series-anomaly-detection-algorithms-1cef5519aef2>

<http://www.johnwittenauer.net/machine-learning-exercises-in-python-part-8/>

<https://qminer.github.io/anomalies/>


<https://www.reddit.com/r/MachineLearning/comments/ko2ij5/p_looking_for_resources_on_anomaly_detection/>


### Remove outliers

https://datascience.stackexchange.com/questions/73274/remove-outliers-from-dataframe-using-pandas-in-python

```
def IQR(data):
    q1 = data['Gbps'].quantile(0.25)
    q3 = data['Gbps'].quantile(0.75)
    iqr = q3 - q1
    fence_low = q1 - 1.5 * iqr
    fence_high = q3 + 1.5 * iqr
    cleaned_data = data.loc[(data['Gbps'] > fence_low) & (data['Gbps'] < fence_high)]
    return cleaned_data

data = {
    'time': ['2018-11-20 00:00:00', 
             '2018-11-20 01:00:00', 
	     '2018-11-20 02:00:00', 
	     '2018-11-20 00:00:00', 
	     '2018-11-20 01:00:00', 
	     '2018-11-20 02:00:00'],
    'Gbps': [ 29.8217476333333333, 
              38.6209872666666667, 
	      0.01, 
	      29.8217476333333333, 
	      38.6209872666666667, 
	      0.0]
}

df1 = pd.DataFrame(data, columns = ['time', 'Gbps'] 
cleaned1 = IQR(df1)
print(cleaned1)
```
https://machinelearningmastery.com/model-based-outlier-detection-and-removal-in-python/

https://machinelearningmastery.com/how-to-use-statistics-to-identify-outliers-in-data/

https://stackoverflow.com/questions/23199796/detect-and-exclude-outliers-in-pandas-data-frame

```
df = pd.DataFrame(np.random.randn(100, 3))

from scipy import stats
df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
```

https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
```
box plot is a method for graphically depicting groups of numerical data through their quartiles.
Box plots may also have lines extending vertically from the boxes (whiskers) 
indicating variability outside the upper and lower quartiles, 
hence the terms box-and-whisker plot and box-and-whisker diagram. 
Outliers may be plotted as individual points.

The interquartile range (IQR), also called the midspread or middle 50%, or technically H-spread, is a measure of statistical dispersion, being equal to the difference between 75th and 25th percentiles, or between upper and lower quartiles, IQR = Q3 − Q1.
In other words, the IQR is the first quartile subtracted from the third quartile; these quartiles can be clearly seen on a box plot on the data.
It is a measure of the dispersion similar to standard deviation or variance, but is much more robust against outliers.
IQR is somewhat similar to Z-score in terms of finding the distribution of data and then keeping some threshold to identify the outlier.

```

https://nextjournal.com/schmudde/how-to-remove-outliers-in-data
```
y = df['rando']
removed_outliers = y.between(y.quantile(.05), y.quantile(.95))

print(str(y[removed_outliers].size) + "/" + str(size) + " data points remain.") 

y[removed_outliers].plot().get_figure()
```

```
df = df[df['item_price']<100000]
df[(np.abs(stats.zscore(df[0])) < 3)]
```
Another example:
```
q = df["col"].quantile(0.99)
df[df["col"] < q]
q_low = df["col"].quantile(0.01)
q_hi  = df["col"].quantile(0.99)

df_filtered = df[(df["col"] < q_hi) & (df["col"] > q_low)]
```


## Isolation Forest

<https://lambda.grofers.com/anomaly-detection-using-isolation-forest-80b3a3d1a9d8>

