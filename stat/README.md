### Основные типы распределений вероятностей в примерах

https://habr.com/ru/articles/801101/

https://habr.com/ru/articles/807051/ Индуктивная статистика: доверительные интервалы, предельные ошибки, размер выборки и проверка гипотез


https://habr.com/ru/articles/217545/ Как правильно лгать с помощью статистики

### Statistical process control
using SQL
https://github.com/jchester/spc-kit

https://news.ycombinator.com/item?id=39612775

### How to generate uniformly random pointson n-spheres and in n-balls

https://extremelearning.com.au/how-to-generate-uniformly-random-points-on-n-spheres-and-n-balls/

https://news.ycombinator.com/item?id=39606371


### краткий обзор  методов выбора случайной точки на диске, на окружности, на сфере и на шаре. 

Во всех этих задачах подразумевается равномерное распределение по поверхности или по объему

https://nabbla1.livejournal.com/95999.html

### Unfair coin - simulate any probability

https://www.alexirpan.com/2015/08/23/simulating-a-biased-coin-with-a-fair-one.html

https://www.quora.com/How-can-I-simulate-a-die-given-a-fair-coin

https://www.quora.com/Can-you-use-a-single-coin-to-simulate-probabilities-like-frac-1-11-Whats-the-minimum-number-of-flips-on-average

https://www.youtube.com/watch?v=lORQ_wt2MZY

https://math.stackexchange.com/questions/3834837/how-to-use-a-fair-coin-to-simulate-any-probability-p-of-winning

### How do you create an event with a probability of 1/3 using an unbiased coin?

https://math.stackexchange.com/questions/3568428/get-1-3-probability-from-a-coin-in-minimal-mean-of-the-amount-of-flips
 
``` 
unbiased coin has P(H) = P(T) = 1/2.
To create the event that the question desires, do follow:
first, understand that P(HH) = P(HT) = P(TH) = P(TT) = 1/4

if you flip coin 2 times in a row:
1) HH happens -> do sth
2) HT happens -> do another stuff
3) TH happens -> do other stuff
4) if TT happens -> reroll coin 2 times again and go back .

This guarantees that we only observe 1/3 events.

 
Toss the unbiased coin thrice. Given the outcome is not both tails ( T T) ,
 then the outcome of both heads (H H) has probability 1/3.
```
### Markov chain
https://arxiv.org/pdf/2207.02296.pdf
###
https://www.statlearning.com/

https://drive.google.com/file/d/1VmkAAGOYCTORq1wxSQqy255qLJjTNvBI/edit?pli=1  Introduction to probability 2nd edition

https://www.thegreatcourses.com/courses/learning-statistics-concepts-and-applications-in-r  Learning Statistics: Concepts and Applications in R

Great links to stat resources
https://news.ycombinator.com/item?id=37854846

https://jasp-stats.org/

### Bayes

https://habr.com/ru/articles/802435/
 
https://xcelab.net/rm/statistical-rethinking/  A Bayesian Course with Examples in R and Stan (& PyMC3 & brms & Julia too

https://users.aalto.fi/~ave/ROS.pdf  Regression and Other Stories

https://openintro-ims2.netlify.app/

https://brilliant.org/courses/statistics/

### queueing-theory

https://github.com/joelparkerhenderson/queueing-theory

https://news.ycombinator.com/item?id=37532439

https://www.cantorsparadise.com/whats-the-probability-of-1-appearing-as-the-first-digit-of-a-number-41f2fcd781c7 
frequency of 1st digit in the number - Benford's law

Hight dimentional probability - Roman Vershinin: 
https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.pdf


https://mltechniques.com/resources/ 

Extreme events in dynamical systems and random walkers: A review
https://arxiv.org/abs/2109.11219

https://habr.com/ru/post/678604/ Viterbi 

https://www.toptal.com/algorithms/metropolis-hastings-bayesian-inference

### How to compare distributions:

https://habr.com/ru/company/skillfactory/blog/674880/

https://habr.com/ru/company/X5Tech/blog/679842/

https://habr.com/ru/company/mygames/blog/677074/


https://github.com/matteocourthoud/Blog-Posts

### Books

Cook book

https://pages.cs.wisc.edu/~tdw/files/cookbook-en.pdf

```
P R O B A B I L I S T I C N U M E R I C S
C O M P U TA T I O N A S  M A C H I N E L E A R N I N G
```
https://www.probabilistic-numerics.org/assets/ProbabilisticNumerics.pdf

https://lukepereira.github.io/notebooks/documents/2021-moduli-attention/main.pdf

### Bayes

https://habr.com/ru/post/658707/

https://habr.com/ru/company/otus/blog/658311/

https://towardsdatascience.com/detect-change-points-with-bayesian-inference-and-pymc3-3b4f3ae6b9bb

https://towardsdatascience.com/a-gentle-intro-to-conjugate-priors-8be6ac0d31f6

https://habr.com/ru/post/598979/

https://www.edx.org/bio/elena-moltchanova . Bayes stat with R

https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/

P(A/B) = P(A) * P(B/A) / P(B)

posterior = prior * (likelihood /marginal)

- Posterior probability (updated probability after the evidence is considered)
- Prior probability (the probability before the evidence is considered)
- Likelihood (probability of the evidence, given the belief is true)
- Marginal probability (probability of the evidence, under any circumstance)

- 1% of women have breast cancer (and therefore 99% do not).
- 80% of mammograms detect breast cancer when it is there (and therefore 20% miss it).
- 9.6% of mammograms detect breast cancer when it’s not there (and therefore 90.4% correctly return a negative result).

Suppose you get a positive test result. What are the chances you have cancer? 

The chances of a true positive = chance you have cancer * chance test caught it = 1% * 80% = .008

The chances of a false positive = chance you don’t have cancer * chance test caught it anyway = 99% * 9.6% = 0.09504

The chance of getting a real, positive result is .008. The chance of getting any type of positive result is the chance of a true positive plus the chance of a false positive (.008 + 0.09504 = .10304).

So, our chance of cancer is .008/.10304 = 0.0776, or about 7.8%.

http://allendowney.github.io/ThinkBayes2/index.html

https://austinrochford.com/posts/2021-06-10-lego-pymc3.html

https://pub.towardsai.net/bayesian-inference-beyond-estimating-statistical-models-4b2f78c7f090


https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf Bayes


http://www.numericalexpert.com/blog/online_stat/ single pass for (variance, skewness, kurtosis, covariance)

http://www.numericalexpert.com/tutorials.php

precision and recall https://habr.com/ru/post/661119/


https://sakshamgulati123.medium.com/an-intuitive-guide-to-various-statistical-tests-d8148105eeca


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

https://patsy.readthedocs.io/en/latest/  Describing statistical models in Python

https://habr.com/ru/post/681218/. statmodels

 
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

https://habr.com/ru/companies/otus/articles/793678/

https://statisticsbyjim.com/basics/z-score

### Correlation

https://towardsdatascience.com/a-new-coefficient-of-correlation-64ae4f260310

https://habr.com/ru/post/683442/

### Casual inference

https://habr.com/ru/company/glowbyte/blog/686398/

https://arxiv.org/abs/2206.15475

https://arxiv.org/abs/2206.15475

https://habr.com/ru/company/ods/blog/544208/

BOOK: Causal Inference for The Brave and True

https://matheusfacure.github.io/python-causality-handbook/landing-page.html

BOOK: Causal Inference in Python
https://www.oreilly.com/library/view/causal-inference-in/9781098140243/

https://microsoft.github.io/dowhy/

https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/

https://www.bradyneal.com/which-causal-inference-book

https://yanirseroussi.com/causal-inference-reading-list/

https://www.inference.vc/causal-inference-4/

### Мир статистических гипотез
https://habr.com/ru/post/558836/ 

https://habr.com/ru/companies/X5Tech/articles/807001/  T-test

### Anova
https://davidbergkamp.com/two-way-anova-tukeys-honest-difference-test/

https://towardsdatascience.com/statistics-in-python-using-anova-for-feature-selection-b4dc876ef4f0
