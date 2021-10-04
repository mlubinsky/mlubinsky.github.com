### Clustering 

https://machinelearningmastery.com/clustering-algorithms-with-python/ 

https://realpython.com/k-means-clustering-python/

https://mubaris.com/2017/10/01/kmeans-clustering-in-python/

https://habrahabr.ru/post/164417/

https://towardsdatascience.com/spectral-clustering-aba2640c0d5b

https://www.youtube.com/watch?v=-_gIcc5_uHY


https://habrahabr.ru/post/322034/ DBSCAN

https://en.wikipedia.org/wiki/DBSCAN  DBSCAN

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
