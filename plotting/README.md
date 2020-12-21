
## BI tools: Poli, SuperSet, etc

<https://github.com/shzlw/poli>

<https://news.ycombinator.com/item?id=20507592> 

https://cloudit-eg.com/data-visualization-tools-to-make-your-data-speak/

<https://datashader.org/>


## PlotJugger, veusz and other tools

https://plotjuggler.io

https://news.ycombinator.com/item?id=25357714

https://kst-plot.kde.org/

<https://veusz.github.io/> VEUSZ

## Observable 
https://news.ycombinator.com/item?id=25161409

### Bokeh

<https://sadanand-singh.github.io/posts/interactivedatavis/> 

https://habr.com/ru/company/skillfactory/blog/526076/

## Python plotting

https://hvplot.holoviz.org/ 

https://pypi.org/project/dtale/

https://towardsdatascience.com/4-libraries-that-can-perform-eda-in-one-line-of-python-code-b13938a06ae
```
Pandas-Profiling
Sweetviz
Autoviz
D-Tale
```


## Lag plot , Autocorrelated plot

https://www.kaggle.com/residentmario/time-series-plotting-optional

https://www.statology.org/autocorrelation-python/

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.autocorr.html

https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/

https://stackoverflow.com/questions/56028461/calculate-autocorrelation-as-a-function-of-lag-in-python

https://pythontic.com/visualization/charts/autocorrelation

https://medium.com/@dganais/autocorrelation-in-time-series-c870e87e8a65

https://www.geeksforgeeks.org/autocorrelation-plot-using-matplotlib/

## Plotline

Book:
https://leanpub.com/plotnine-guide

https://datascienceworkshops.com/blog/plotnine-grammar-of-graphics-for-python/

https://www.practicaldatascience.org/html/plotting_part2.html


<https://github.com/has2k1/plotnine> as ggplot2

https://realpython.com/ggplot-python/

https://www.kaggle.com/residentmario/grammar-of-graphics-with-plotnine-optional

https://github.com/has2k1/plotnine-examples/blob/master/plotnine_examples/examples/facet_grid.ipynb

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


 



### Pywedge
https://towardsdatascience.com/pywedge-a-complete-package-for-eda-data-preprocessing-and-modelling-32171702a1e0

https://pypi.org/project/pywedge/

<https://github.com/JetBrains/lets-plot/blob/master/README_PYTHON.md> as ggplot2

<https://view.datalore.jetbrains.com/notebook/v8mLoENq8XTfmStTCLNMV6> seaborn

<https://soliddata.io/index.php/2020/03/31/how-to-do-data-visualization-with-python/> seaborn

<https://towardsdatascience.com/plotting-with-python-c2561b8c0f1f>

<http://pyviz.org/>

<http://vispy.org/>

<https://habr.com/ru/post/468295/> matplotlib

## Visidata
http://visidata.org/ .  can read parquet

https://jsvine.github.io/intro-to-visidata/the-big-picture/visidata-in-60-seconds/

https://www.youtube.com/watch?v=N1CBDTgGtOU&list=PLxu7QdBkC7drrAGfYzatPGVHIpv4Et46W


http://blog.pyviz.org/

<https://kst-plot.kde.org/>  real-time large-dataset viewing and plotting

<https://plotnine.readthedocs.io/en/stable/>

<https://www.reddit.com/r/Python/comments/bkyeyc/the_reason_i_am_using_altair_for_most_of_my/>  Altair

<https://mlwhiz.com/blog/2019/04/19/awesome_seaborn_visuals/> .  seaborn

<https://github.com/mcastorina/graph-cli> .  plottting from CSV

<https://habr.com/post/431754/> Dash

<https://medium.com/swlh/effective-visualization-of-multi-dimensional-data-a-hands-on-approach-b48f36a56ee8>

<https://www.anaconda.com/blog/developer-blog/python-data-visualization-2018-why-so-many-libraries/>

<https://kite.com/blog/python/data-analysis-visualization-python>

<https://codeburst.io/overview-of-python-data-visualization-tools-e32e1f716d10>

<https://youtu.be/FytuB8nFHPQ>

<http://pbpython.com/python-vis-flowchart.html>

<https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/>





<https://altair-viz.github.io/> .  

<http://holoviews.org/>

<https://python-graph-gallery.com/>

<https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f>


<https://youtu.be/psvU4zwO3Ao> . Plotly


## ELK: Elastic Search, Logstash,  Kibana

<https://habr.com/ru/post/443528/>




### Visualization on desktop

<https://wci.llnl.gov/simulation/computer-codes/visit>

<https://veusz.github.io/>

<http://www.wizardmac.com/>

<https://habr.com/company/pixonic/blog/414921/>  Apache Zeppelin

<https://www.knime.com/>

https://rapidminer.com/

https://sourceforge.net/projects/weka/

https://orange.biolab.si/

https://elki-project.github.io/
	


https://www.kaggle.com/learn/data-visualisation

http://hypertools.readthedocs.io/en/latest/index.html	


https://datavizcatalogue.com/

http://datavizproject.com/

https://github.com/PAIR-code/facets

https://github.com/timkpaine/lantern

https://github.com/mlubinsky/chart

https://movio.co/en/blog/improving-with-sql-and-charts/

https://github.com/MLWave/kepler-mapper

## Matplotlib

<https://habr.com/ru/post/468295/>

<https://realpython.com/python-matplotlib-guide/>

<https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f>

<https://nbviewer.jupyter.org/urls/gist.githubusercontent.com/Jwink3101/e6b57eba3beca4b05ec146d9e38fc839/raw/f486ca3dcad44c33fc4e7ddedc1f83b82c02b492/Matplotlib_Cheatsheet>

<http://blog.adnansiddiqi.me/tag/matplotlib/>

https://medium.com/@kbrook10/day-4-data-visualization-how-to-use-seaborn-for-heatmaps-bf8070e3846e Heatmap

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

[create an anchor](#anchors-in-markdown)
