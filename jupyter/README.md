# Jupyter Pandas NumPy Scikit

 Jake Vanderplas . <https://jakevdp.github.io/PythonDataScienceHandbook/>
 
## Plotting the time series
<https://machinelearningmastery.com/time-series-data-visualization-with-python/>

<https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html>

```
from datetime import datetime
# example of formatting
date = datetime.strptime('01 Jan 2016', '%d %b %Y')
print(date)
date = datetime.strptime('2017-05-04',"%Y-%m-%d")
print(date)

# generate the date objects: 2 points per day  for entire year
from datetime import timedelta  
i=0
times=[]
v=[]
date = datetime.strptime('01 Jan 2016', '%d %b %Y')

while i < 365:
  new_date= date+timedelta(hours=i*12) 
  print (i, new_date, new_date.month)  # new point every 12 hours
  times.append(new_date)
  v.append ( new_date.month)
  i+=1  
  
  
df = pd.DataFrame({'keys':times,'vals':v})  

# Grouping

# Group by Month
df.index=df["keys"]
per_month=df.groupby(pd.Grouper(freq='M'))

print (type(per_month))
print (per_month.sum())
print (type(per_month.sum()))

# Group by Day
per_day=df.groupby(pd.Grouper(freq='D'))
# per_day= df.resample('D').sum().plot() --- consider this instead line above, what is the difference ???

print (type(per_day))         # DataFrameGroupBy
print (per_day.sum())          
print (type(per_day.sum()))   # DataFrame 

per_day_sum=per_day.sum()

#   Plotting

import matplotlib.pyplot as plt

## Plot 1
per_day_sum.plot()

## Plot 2
df.resample('D').sum().plot()  

## Plot 3
X=per_day_sum.index
Y=per_day_sum.values
plt.plot(X,Y)
plt.show() . # issue - ticks and X labels

## Split data in separate dataframes per month
first_days = [
  datetime.date (2016, 1,1),
  datetime.date (2016, 2,1),
  datetime.date (2016, 3,1),
  datetime.date (2016, 4,1),
  datetime.date (2016, 5,1),
  datetime.date (2016, 6,1),
  datetime.date (2016, 7,1),
  datetime.date (2016, 8,1),
  datetime.date (2016, 9,1),
  datetime.date (2016, 10,1),
  datetime.date (2016, 11,1),
  datetime.date (2016, 12,1)
  ]
  
  
from pandas.tseries.offsets import MonthEnd
from datetime import timedelta 

per_month=pd.DataFrame()
for first_day in first_days:
    last_day=first_day+MonthEnd(1)+timedelta(hours=23, minutes=59, seconds=59)
    m=first_day.strftime('%b') . # human-readable month
    per_month[m]=per_day_sum[first_day : last_day]
    
per_month.plot(subplots=True, legend=True)
plt.show()
```

## Group By
<http://cmdlinetips.com/2019/03/how-to-write-pandas-groupby-function-using-sparse-matrix/>


https://www.kaggle.com/learn/overview  Pandas, TensorFlow, etc

<https://github.com/Yorko/mlcourse_open/tree/master/jupyter_russian>     Jupiter Russian notebooks

<https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#statistics-machine-learning-and-data-science>

<https://radimrehurek.com/data_science_python/>

<https://github.com/hangtwenty/dive-into-machine-learning>

<https://sadanand-singh.github.io/posts/pyplotsmultivariables/>


## Scikit-learn
<https://medium.com/analytics-vidhya/scikit-learn-a-silver-bullet-for-basic-machine-learning-13c7d8b248ee>

<https://www.youtube.com/watch?v=L7R4HUQ-eQ0>

<http://scikit-learn.org/stable/tutorial/>

<https://www.interviewqs.com/blog/intro_to_scikit_learn>

<https://stackoverflow.com/questions/40845304/runtimewarning-numpy-dtype-size-changed-may-indicate-binary-incompatibility>

## Linear model
```
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
```
```
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
# data:
ar = np.array([[[1],[2],[3]], [[2],[4],[6]]]) # y=2*x
x = ar[0,:]
y = ar[1,:]

reg = linear_model.LinearRegression()
reg.fit(x,y)
print('Coefficients: \n', reg.coef_)

xTest = np.array([[4],[5],[6]])
ytest =  np.array([[8],[10],[12]])
preds = reg.predict(xTest)
print("Mean squared error: %.2f" % mean_squared_error(ytest,preds))
print("Variance score: %.2f" % r2_score(ytest,preds))
plt.scatter(xTest,preds, color='black')
plt.plot(xTest,preds,color='blue', linewidth=3)

plt.show()
```

## NumPy 
```
http://scipy.github.io/old-wiki/pages/NumPy_for_Matlab_Users.html
https://realpython.com/numpy-array-programming/	
http://nbviewer.jupyter.org/github/vlad17/np-learn/blob/master/presentation.ipynb?flush_cache=true NumPy
http://www.labri.fr/perso/nrougier/from-python-to-numpy/
https://docs.scipy.org/doc/numpy-1.10.0/user/basics.broadcasting.html
https://www.analyticsvidhya.com/blog/2017/02/top-28-cheat-sheets-for-machine-learning-data-science-probability-sql-big-data/
http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html
https://www.datacamp.com/community/tutorials/python-numpy-tutorial
https://www.dataquest.io/blog/numpy-tutorial-python/
https://www.python-course.eu/numpy.php
https://github.com/Kyubyong/numpy_exercises
http://heydenberk.com/blog/posts/demystifying-pandas-numpy-filtering/
http://cs231n.github.io/python-numpy-tutorial/
https://github.com/HIPS/autograd
https://www.machinelearningplus.com/101-numpy-exercises-python/
```
## Pandas
```
https://stackoverflow.com/questions/29432629/correlation-matrix-using-pandas

http://www.dataschool.io/easier-data-analysis-with-pandas/
https://news.ycombinator.com/item?id=16473482
http://nbviewer.jupyter.org/github/pybokeh/jupyter_notebooks/blob/master/pandas/PandasCheatSheet.ipynb
https://jakevdp.github.io/PythonDataScienceHandbook/
https://www.kaggle.com/learn/data-visualisation
https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
https://spapas.github.io/2016/09/21/pandas-pivot-table-primer/
https://github.com/JosPolfliet/pandas-profiling
https://www.dataquest.io/blog/pandas-concatenation-tutorial/
https://towardsdatascience.com/how-to-learn-pandas-108905ab4955
http://blog.enthought.com/python/pandas/cheat-sheets-pandas-the-python-data-analysis-library/#.WjSdBlQ-dp9
https://habrahabr.ru/company/ods/blog/322626/
https://www.dataquest.io/blog/pandas-big-data/
https://www.dataquest.io/blog/machine-learning-python/
https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python
http://hypertools.readthedocs.io/en/latest/index.html
	
http://www.zavtech.com/morpheus/docs/  DataFrames in Java
```
