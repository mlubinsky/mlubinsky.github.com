```
There is Python pandas dataframe with following columns:

- date ( string in format YYYY-MM-DD)

- device (string)

- build (string)

- metric (string)

- number (float).

For every date in dataframe there are many builds, metrics and devices.

Please create separate bar chart for every metric value in dataframe.

The x-axis should be the build column and the y-axis is average(number) per build.

All bars should have a different colors  per build and the legend should provide the mapping between the

build and the bar color  
```
Gemini:
```
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have your DataFrame named 'df'
# Replace 'your_data.csv' with your actual file path if using a CSV
# df = pd.read_csv('your_data.csv')

# Group by metric and build, calculate average number
grouped_data = df.groupby(['metric', 'build'])['number'].mean().reset_index()

# Unique metrics for iteration
unique_metrics = grouped_data['metric'].unique()

# Create a separate bar chart for each metric
for metric in unique_metrics:
    filtered_data = grouped_data[grouped_data['metric'] == metric]

    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['build'], filtered_data['number'], color=plt.cm.tab20(range(len(filtered_data))))
    plt.title(f"Average Number per Build for Metric: {metric}")
    plt.xlabel("Build")
    plt.ylabel("Average Number")

    # Create a legend
    legend_labels = [f"{build}: {color}" for build, color in zip(filtered_data['build'], plt.cm.tab20(range(len(filtered_data))))]
    plt.legend(legend_labels, title="Build Legend")

    plt.show()

```

Dataframe with following columns:
 - date ( string in format YYYY-MM-DD)
 - device (string)
 - build (string)
 - metric (string)
 - number (float)

For every date in dataframe there are many builds, metrics and devices.

Input: date range

TODO:
```
Bar chart #1 (per metric): 
Title: date range
x-axis: date
y-axis: avg(number) per build 

Bar chart #2 (per metric):
x-axis: build
y-axis: avg(number) per build 
```



https://pyvista.org/  (on top of VTK)

https://python-graph-gallery.com/

https://habr.com/ru/companies/astralinux/articles/814881/ HoloViews + Flask

https://holoviews.org/user_guide/Deploying_Bokeh_Apps.html#combining-bokeh-application-and-flask-application

https://github.com/rougier/scientific-visualization-book .  BOOK!

https://habr.com/ru/companies/ru_mts/articles/738208/ Plotting

https://habr.com/ru/companies/ru_mts/articles/738208/ matplotlib

https://github.com/TutteInstitute/datamapplot

https://towardsdatascience.com/professionally-visualize-data-distributions-in-python-09481e1493b2

https://python.plainenglish.io/data-visualization-for-exploratory-data-analysis-eda-in-python-4aea402648e7

https://towardsdatascience.com/declarative-vs-imperative-plotting-3ee9952d6bf3

### Visro
https://github.com/mckinsey/vizro

## PyVis

https://medium.com/@stephanhausberg/graph-networks-visualization-with-pyvis-and-keyword-extraction-cd973d372e2c

https://github.com/garrettj403/SciencePlots

https://lets-plot.org/

https://proplot.readthedocs.io/en/stable/ proplot

https://dataviz.dylancastillo.co/

https://habr.com/ru/company/otus/blog/682500/.  Python based dashboards

https://www.youtube.com/watch?v=cTJBJH8hacc matplotlib tutorial

https://github.com/ponnhide/patchworklib subplot manager

https://github.com/lux-org/lux

https://towardsdatascience.com/the-easiest-way-to-make-beautiful-interactive-visualizations-with-pandas-cdf6d5e91757

https://sophiamyang.github.io/DS/visualization/holoviz/holoviz.html


https://shiny.rstudio.com/py/ 
### EDA 


https://www.zenrows.com/blog/exploratory-data-analysis-in-python

https://towardsdatascience.com/exploratory-sensor-data-analysis-in-python-3a26d6931e67

https://towardsdatascience.com/exploratory-data-analysis-visualization-and-prediction-model-in-python-241b954e1731


https://towardsdatascience.com/complete-guide-to-data-visualization-with-python-2dd74df12b5e

https://github.com/marcskovmadsen/panel-highcharts

https://xcorr.net/2021/06/02/dynamic-scientific-visualizations-in-the-browser-for-python-users/

https://github.com/rougier/scientific-visualization-book

https://plotly.com/python/

https://pypi.org/project/autoplotter/ (using Dash)

https://pypi.org/project/sweetviz/

https://geekyhumans.com/draw-various-types-of-charts-and-graphs-using-python/ Matplotlib and Plotly

https://habr.com/ru/company/otus/blog/558478/

https://python-graph-gallery.com/ Pandas, Seaborn, Matplotlib examples!

https://pythonplot.com/  Pandas, Seaborn, Matplotlib examples!

https://matplotlib.org/stable/gallery/index.html Matplotlib examples

https://towardsdatascience.com/a-practical-summary-of-matplotlib-in-13-python-snippets-4d07f0011bdf

https://github.com/matplotlib/cheatsheets

https://machinelearningmastery.com/seaborn-data-visualization-for-machine-learning

https://habr.com/ru/post/557424/

https://github.com/antonlopezr/mpl_plotter

https://medium.com/codex/beyond-matplotlib-and-seaborn-python-data-visualization-tools-that-work-3ef7f8d1500e

https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/

https://www.practicaldatascience.org/html/plotting_part2.html



https://stackabuse.com/matplotlib-draw-vertical-lines-on-plot/ vertical line in matplotlib

https://towardsdatascience.com/a-simple-guide-to-beautiful-visualizations-in-python-f564e6b9d392

https://pypi.org/project/dama/

http://pyviz.org/

http://vispy.org/

https://datavizcatalogue.com/

http://datavizproject.com/

https://towardsdatascience.com/plotting-with-python-c2561b8c0f1f

https://kite.com/blog/python/data-analysis-visualization-python

## Python plotting code examples

https://towardsdatascience.com/advanced-pandas-plots-e2347a33d576 . Advanced Pandas Plots

https://www.youtube.com/watch?v=mZOIeOeswB0


https://pythonplot.com/

https://python-graph-gallery.com/

https://cmdlinetips.com/2020/01/tips-to-make-common-plots-with-pandas/

https://www.kite.com/blog/python/data-analysis-visualization-python/

https://github.com/lux-org/lux

### HVPLOT
https://hvplot.holoviz.org/ hvplot !!!

https://github.com/antonlopezr/mpl_plotter

## Seaborn

http://seaborn.pydata.org/examples/index.html

https://habr.com/ru/company/otus/blog/540526/

<https://view.datalore.jetbrains.com/notebook/v8mLoENq8XTfmStTCLNMV6> seaborn

<https://soliddata.io/index.php/2020/03/31/how-to-do-data-visualization-with-python/> seaborn

<https://mlwhiz.com/blog/2019/04/19/awesome_seaborn_visuals/> .  seaborn


https://jbencook.com/pandas-melt/    pd.melt(wide_df)

https://jbencook.com/seaborn-histogram/

To see multiple distributions in the same plot. 
If your Pandas DataFrame is in long format, 
you can do this by passing in a categorical column to the hue argument:
```
ax = sns.histplot(df, x="revenue", bins=30, stat="probability", hue="region")
ax.set(ylabel="$p(x)$")
```
## Pandas plotting 

https://opendatascience.com/how-to-pivot-and-plot-data-with-pandas/

https://cmdlinetips.com/2020/01/tips-to-make-common-plots-with-pandas/

https://jbencook.com/pandas-melt/

https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook-plotting

https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html


https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/

https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot

 
Line plot, multiple columns:
Just reuse the Axes object.
```
import matplotlib.pyplot as plt
import pandas as pd

# gca stands for 'get current axis'
ax = plt.gca()

df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

plt.show()
```

## Pivot, pivot_table() and transpose()

https://opendatascience.com/how-to-pivot-and-plot-data-with-pandas/

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html

df.pivot(index='hour', columns='dayname', values="MB").plot(title=header)

df2=pd.pivot_table(df, index=['date'], columns='company' values='MB'  )

## Heatmaps

https://blog.algorexhealth.com/2017/09/10-heatmaps-10-python-libraries/

https://medium.com/@kbrook10/day-4-data-visualization-how-to-use-seaborn-for-heatmaps-bf8070e3846e Heatmap


### Heatmaps in plotnine

https://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_tile.html

https://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_bin2d.html


### Lag plot , Autocorrelated plot

https://www.kaggle.com/residentmario/time-series-plotting-optional

https://www.statology.org/autocorrelation-python/

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.autocorr.html

https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/

https://stackoverflow.com/questions/56028461/calculate-autocorrelation-as-a-function-of-lag-in-python

https://pythontic.com/visualization/charts/autocorrelation

https://medium.com/@dganais/autocorrelation-in-time-series-c870e87e8a65

https://www.geeksforgeeks.org/autocorrelation-plot-using-matplotlib/


## Matplotlib

https://github.com/rougier/matplotlib-tutorial

https://github.com/rougier/scientific-visualization-book

<https://habr.com/ru/post/468295/>

<https://realpython.com/python-matplotlib-guide/>

<https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f>

<https://nbviewer.jupyter.org/urls/gist.githubusercontent.com/Jwink3101/e6b57eba3beca4b05ec146d9e38fc839/raw/f486ca3dcad44c33fc4e7ddedc1f83b82c02b492/Matplotlib_Cheatsheet>

<http://blog.adnansiddiqi.me/tag/matplotlib/>

https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section0_2-Plotting-and-Visualization.ipynb

https://medium.com/100-free-udemy-coupons/udemy-making-graphs-in-python-using-matplotlib-for-beginners-free-be3df23bdabe

https://github.com/matplotlib/AnatomyOfMatplotlib

http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html

https://www.numfocus.org/blog/matplotlib-lead-developer-explains-why-he-cant-fix-the-docs-but-you-can/

<https://github.com/antonkorbalev/simplesysmon>  Matplotlib +  Flask

http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these

http://hypertools.readthedocs.io/en/latest/index.html
	
https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4

<https://www.youtube.com/watch?v=z7ZINBk8EUk&list=PL998lXKj66MpNd0_XkEXwzTGPxY2jYM2d>

<https://habr.com/ru/post/468295/> matplotlib

<https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f>

<https://github.com/mcastorina/graph-cli> .  plottting from CSV



### Plotnine

https://evamaerey.github.io/ggplot_flipbook/ggplot_flipbook_xaringan.html#1

https://youtu.be/z6xNKZZMWgU

<https://plotnine.readthedocs.io/en/stable/> 

https://github.com/has2k1/plotnine-examples/

<https://leanpub.com/plotnine-guide> . book

https://dputhier.github.io/jgb53d-bd-prog_github/practicals/intro_ggplot/intro_ggplot.html

https://datascienceworkshops.com/blog/plotnine-grammar-of-graphics-for-python/

https://www.practicaldatascience.org/html/plotting_part2.html

<https://github.com/has2k1/plotnine> as ggplot2

https://realpython.com/ggplot-python/

https://www.kaggle.com/residentmario/grammar-of-graphics-with-plotnine-optional

https://github.com/has2k1/plotnine-examples/blob/master/plotnine_examples/examples/facet_grid.ipynb

<https://towardsdatascience.com/how-to-use-ggplot2-in-python-74ab8adec129>

what is hstack?
```
 import numpy as np
 x=np.array((3,5,7))
 y=np.array((30,50,70))
 np.hstack((x,y))
 array([ 3,  5,  7, 30, 50, 70])
 xx=np.array([[3],[5],[7]])
>>> xx
array([[3],
       [5],
       [7]])
yy=np.array([[30],[50],[70]])
>>> np.hstack((xx,yy))
array([[ 3, 30],
       [ 5, 50],
       [ 7, 70]])

```
Plotnine works best with tidy data, i.e each variable is a column and each observation a row.
https://stackoverflow.com/questions/62900745/how-to-add-legend-in-ggplot-plotnine-for-multiple-curves
```
from plotnine import *
import numpy as np
import pandas as pd

str_metric = 'metric'
metric = np.array([0.127, 0.1715, 0.19166667, 0.21583333, 0.24866667, 0.24216667, 0.24433333,
                   0.255, 0.291, 0.30966667, 0.32033333, 0.2415, 0.33833333, 0.30583333, 0.34433333])

metric2 = metric * 2

iterations2 = [i for i in range(len(metric))]

# tidy data
df = pd.DataFrame({
    'iterations': np.hstack([iterations2, iterations2]),
    'value': np.hstack([metric, metric2]),
    'type': np.repeat(['metric', 'metric2'], len(iterations2))   
})

p = (ggplot(df, 
     aes(x='iterations', y='value', color='type'))
     + geom_smooth(method='lm', span=0.10, se=True, level=0.80)
     # Then you can change the colour using a scale
    )
```    



### facet grid and other examples:
 
https://github.com/has2k1/plotnine-examples/tree/master/plotnine_examples 

Facet a discrete variable into rows: 
```
facet_grid('drv ~ .')
```
Facet a discrete variable into columns:
```
facet_grid('. ~ cyl')
```

Facet two discrete variables into rows and columns:
```
facet_grid('drv ~ cyl')
```

You can choose if the scale of x- and y-axes are fixed or variable by using the scales argument within the facet_grid() command:
```
(
    ggplot(mpg, aes(x='displ', y='hwy')) 
    + geom_point()
    + facet_grid('drv ~ .', scales = 'free')
    + labs(x='displacement', y='horsepower')
)
```

2-dimentional grid
```
facet_grid('drv + transmission ~ .')
```


https://www.anaconda.com/blog/developer-blog/python-data-visualization-2018-why-so-many-libraries/

https://codeburst.io/overview-of-python-data-visualization-tools-e32e1f716d10

https://youtu.be/FytuB8nFHPQ

http://pbpython.com/python-vis-flowchart.html


### Pywedge
https://towardsdatascience.com/pywedge-a-complete-package-for-eda-data-preprocessing-and-modelling-32171702a1e0

https://pypi.org/project/pywedge/

<https://github.com/JetBrains/lets-plot/blob/master/README_PYTHON.md> as ggplot2


### Datapane 
is a Python framework for building beautiful data science documents for your company, clients, or community.
<https://datapane.com>

<http://haifengl.github.io/vegalite.html>
