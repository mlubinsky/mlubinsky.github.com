https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf Bayes


http://www.numericalexpert.com/blog/online_stat/ single pass for (variance, skewness, kurtosis, covariance)

http://www.numericalexpert.com/tutorials.php


### Permutations

The number of permutations of n distinct objects is n!

### combinations = сочетание
  сочетанием из   n по   k называется набор из   k элементов, выбранных из   n-элементного множества, 
  в котором не учитывается порядок элементов.

combination is a selection of items from a set that has distinct members, 
such that the order of selection does not matter 

If the set has n elements, the number of k-combinations, denoted as  C_{k}^{n}} C_{k}^{n}, is equal to the binomial coefficient C= n!/k!(n-k)!

### Размещение = k-permutations of n

размеще́нием (из n по k) называется упорядоченный набор из k различных элементов из некоторого множества различных n элементов.  В отличие от сочетаний, размещения учитывают порядок следования предметов.

A= n!/k!(n-k)!

### Python

https://patsy.readthedocs.io/en/

if we have some variable y, and we want to regress it against some other variables x, a, b, and the interaction of a and b, then we simply write:

patsy.dmatrices("y ~ x + a + b + a:b", data)

https://cdanielaam.medium.com/essential-mathematical-equations-for-predictive-models-fcb79630ec96

https://habr.com/ru/post/585232/  Получаем кривую плотности распределения вероятности

https://habr.com/ru/post/587372/ Получаем кривую плотности распределения вероятности случайного процесса

https://habr.com/ru/post/556856/   Python и статистический вывод: часть 4

https://habr.com/ru/post/562380/ Погружаемся в статистику вместе с Python

https://towardsdatascience.com/probability-distributions-with-pythons-scipy-3da89bf60565

https://towardsdatascience.com/statistical-modelling-with-python-the-three-must-know-s-modules-79fa393e5640 

https://www.kdnuggets.com/2021/09/advanced-statistical-concepts-data-science.html

https://www.kdnuggets.com/2021/09/determine-best-fitting-data-distribution-python.html

https://towardsdatascience.com/a-practical-introduction-to-9-regression-algorithms-389057f86eb9 

https://towardsdatascience.com/deep-diving-statistical-distributions-with-python-for-data-scientists-a0a4badc8d1a  
https://towardsdatascience.com/random-seed-numpy-786cf7876a5f


https://towardsdatascience.com/practical-guide-to-common-probability-distributions-in-machine-learning-487f6137625

https://towardsdatascience.com/practical-guide-to-common-probability-distributions-in-machine-learning-part-2-5bcb910218c0 

https://towardsdatascience.com/statistics-in-python-generating-random-numbers-in-python-numpy-and-sklearn-60e16b2210ae 


https://towardsdatascience.com/mathematical-statistics-a-rigorous-derivation-and-analysis-of-the-wald-test-score-test-and-6262bed53c55 

https://towardsdatascience.com/union-of-probabilistic-event-groups-b415d23e1a62 

## Stat

https://www.statlearning.com/

https://www.crosstab.io/

https://xcelab.net/rm/statistical-rethinking/

http://bayes.cs.ucla.edu/WHY/ The Book of why

 five number summary in statistics: 
 mean, 
 median, 
 standard deviation, 
 25th percentile and 
 75th percentile.
 
 interquartile range - IQR is 75th - 25th, aka, the middle-50%
 
 
https://habr.com/ru/post/548104/ ТЕСТ МАННА-УИТНИ-УИЛКОКСОНА И SCORE-ФУНКЦИИ

https://seeing-theory.brown.edu/index.html

http://www.jerrydallal.com/LHSP/LHSP.HTM

https://www.stat.berkeley.edu/~aditya/resources/AllLectures2018Fall201A.pdf

https://habr.com/post/265321/ . statistical disributions

https://seeing-theory.brown.edu/index.html . Visual probability and stat

https://textbooks.opensuny.org/introduction-to-the-modeling-and-analysis-of-complex-systems/

https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf

https://github.com/Quanteeks/Statistics-lectures/blob/master/book.pdf 
 
 

https://queueing-tool.readthedocs.io/en/latest/

https://www.youtube.com/watch?v=pYxNSUDSFH4  Probability vs likehood

https://www.dynatrace.com/news/blog/why-averages-suck-and-percentiles-are-great/

https://www.youtube.com/watch?v=coNDCIMH8bk

"How NOT to Measure Latency"

https://www.infoq.com/presentations/latency-response-time/

https://github.com/astralord/Statistics-lectures/blob/master/book.pdf

https://openintro-ims.netlify.app/ Modern stat book

https://www.dynatrace.com/news/blog/why-averages-suck-and-percentiles-are-great/

https://www.infoq.com/presentations/latency-response-time/

https://towardsdatascience.com/all-probability-distributions-explained-in-six-minutes-fe57b1d49600

https://www.maa.org/sites/default/files/pdf/ebooks/GTE_sample.pdf

https://github.com/telmo-correa/all-of-statistics

In the case of normally distributed data,
the three sigma rule means that roughly 1 in 22 observations will differ by twice the standard deviation or more from the mean,
and 1 in 370 will deviate by three times the standard deviation

https://statmodeling.stat.columbia.edu/2020/12/09/what-are-the-most-important-statistical-ideas-of-the-past-50-years/

	How percentile approximation works and why it's more useful than averages 
https://news.ycombinator.com/item?id=28526966

### survival analysis
https://www.crosstab.io/topics/survival-analysis

https://www.crosstab.io/articles/survival-analysis-applications

### Z-score

https://statisticsbyjim.com/basics/z-score

### Bayes

http://allendowney.github.io/ThinkBayes2/index.html

https://austinrochford.com/posts/2021-06-10-lego-pymc3.html

https://pub.towardsai.net/bayesian-inference-beyond-estimating-statistical-models-4b2f78c7f090


### Casual inference
https://matheusfacure.github.io/python-causality-handbook/landing-page.html

https://microsoft.github.io/dowhy/

https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/

https://www.bradyneal.com/which-causal-inference-book

https://yanirseroussi.com/causal-inference-reading-list/

https://www.inference.vc/causal-inference-4/

### Мир статистических гипотез
https://habr.com/ru/post/558836/ 



### Anova
https://davidbergkamp.com/two-way-anova-tukeys-honest-difference-test/
