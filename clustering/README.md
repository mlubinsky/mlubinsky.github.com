### Clustering 

<https://habr.com/ru/companies/spbifmo/articles/781710/> Sparkling: Открытая библиотека для автоматического решения задачи кластеризации табличных и мультимодальных данных

https://habr.com/ru/companies/skillfactory/articles/714304/

https://habr.com/ru/articles/784868/



https://habr.com/ru/articles/829202/ алгоритм K-means++

https://habr.com/ru/companies/skillfactory/articles/877684/

https://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set

https://arxiv.org/pdf/2006.04916.pdf

```
The 'elbow method' is a heuristic (a subjective rule of thumb) rather than a statistic.
 A more mathematically rigorous and defensible approach is the Gap Statistic.
If I am your boss, I will expect and ask you for the Gap stat, because we may need to explain and >defend< our analysis.
 "I simply eye-balled it" 👁️ won't cut it when we are under the spotlight.
But before you cluster, you must determine whether there are clusters in the dataset.
To test for that, you use the Hopkins statistic. You must do this for clustering algorithms will cluster even random white-noise.
Finally, once you cluster you should also try K-Medoids and see which of the two, K-Medoids or K-Means, is a better fit.
K-Means is intolerant of outliers.
```

https://machinelearningmastery.com/clustering-algorithms-with-python/ 

https://realpython.com/k-means-clustering-python/

https://mubaris.com/2017/10/01/kmeans-clustering-in-python/

https://habrahabr.ru/post/164417/

https://lazypredict.readthedocs.io/en/latest/readme.html#

https://towardsdatascience.com/spectral-clustering-aba2640c0d5b

https://www.youtube.com/watch?v=-_gIcc5_uHY

### DBSCAN
https://habrahabr.ru/post/322034/ DBSCAN

https://en.wikipedia.org/wiki/DBSCAN  DBSCAN

https://habr.com/ru/articles/818889/ Сравниваем DBSCAN и OPTICS

https://towardsdatascience.com/a-gentle-introduction-to-hdbscan-and-density-based-clustering-5fd79329c1e8


SciPy Hierarchical Clustering and Dendrogram Tutorial
	
https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/


https://martinfleischmann.net/clustergam-visualisation-of-cluster-analysis/


X-means  http://docs.splunk.com/Documentation/MLApp/3.4.0/User/Algorithms#X-means

```
Алгоритм кластеризации X-means представляет собой расширенный алгоритм k-means, 
который автоматически определяет количество кластеров на основе информационного байесовского критерия (BIC). 
Этот алгоритм удобно использовать, когда нет предварительной информации о числе кластеров, 
на которые эти данные могут быть разделены. 

RobustScaler http://docs.splunk.com/Documentation/MLApp/3.4.0/User/Algorithms#RobustScaler

Это алгоритм предварительной обработки данных. По применению схож с алгоритмом StandardScaler, 
который преобразует данные так, что для каждого признака среднее будет равно 0, а дисперсия будет равна 1, в
результате чего все признаки будут иметь один и тот же масштаб. 
Однако это масштабирование не гарантирует получение каких-то конкретных минимальных и максимальных значений признаков. 
RobustScaler аналогичен StandardScaler в том плане, что в результате его применения признаки будут иметь один и тот же масштаб. 
Однако RobustScaler вместо среднего и дисперсии использует медиану и квартили. 
Это позволяет RobustScaler игнорировать выбросы или ошибки измерений, которые могут стать проблемой для остальных методов 
масштабирования.
```
