
https://habr.com/ru/post/653363/ . [Часть 1] Математика в АБ-тестах. Что такое z-score и p-value?

https://habr.com/ru/companies/otus/articles/815769/

https://habr.com/ru/articles/781060/

https://habr.com/ru/companies/sbermarket/articles/774608/

https://habr.com/ru/articles/772940/  проверять сразу несколько гипотез на одном и том же наборе данных

https://habr.com/ru/companies/X5Tech/articles/768008/ 

https://posthog.com/blog/ab-testing-mistakes

https://posthog.com/blog/ab-testing-mistakes

https://habr.com/ru/companies/ozontech/articles/738318/ bandits

https://habr.com/ru/company/vk/blog/673914/ bandits

https://habr.com/ru/post/558836/ Мир статистических гипотез

https://habr.com/ru/company/mygames/blog/677074/ x2 text

https://vkteam.medium.com/practitioners-guide-to-statistical-tests-ed2d580ef04f

https://habr.com/ru/company/plarium/blog/526706/

https://habr.com/ru/company/mailru/blog/557308/

https://habr.com/ru/post/554194/

https://news.ycombinator.com/item?id=25014901 Bayes vs. Freq

https://rpsychologist.com/d3/nhst/

<https://en.wikipedia.org/wiki/Test_statistic>

<http://bytepawn.com/tag/ab-testing.html>

<https://habr.com/ru/company/boodet_online/blog/498688/>  

https://habr.com/ru/company/X5Group/blog/596279/

## Churn rate + Retention = 100 %
https://www.sisense.com/blog/how-to-calculate-cohort-retention-in-sql/

https://www.sisense.com/blog/use-self-joins-to-calculate-your-retention-churn-and-reactivation-metrics/

https://dzone.com/articles/a-guide-for-customer-retention-analysis-with-sql

https://www.holistics.io/blog/calculate-cohort-retention-analysis-with-sql/

https://ubiq.co/database-blog/how-to-calculate-retention-rate-in-sql/

https://stackoverflow.com/questions/56409832/how-to-produce-a-customer-retention-table-cohort-analysis-with-sql

https://mherman.org/blog/cohort-analysis-data-sourcing-with-sql/

https://excelkingdom.blogspot.com/2019/01/how-to-do-customers-retention-analysis.html

https://www.linkedin.com/pulse/use-cases-sql-window-functions-case-2-daily-retention-vladimir-ryzhov

https://dba.stackexchange.com/questions/244833/how-to-calculate-month-over-month-user-retention-based-on-already-active-users

https://chartio.com/resources/tutorials/performing-cohort-analysis-using-mysql/

```
Rolling retention is defined as the percentage of returning users measure at a regular interval, 
typical weekly or monthly, grouped by their sign-up week/month, also known as cohort. 
By grouping users based on when they signed up, 
you can gain insight on how your product/marketing/sales initiatives have impacted retention: 
For example, suppose you had a major launch and had many sign-ups over the following few days. 
How well did these new users stick around compared to, say, pre-launch users that signed up a week prior? 
```
https://blog.treasuredata.com/blog/2016/07/22/rolling-retention-done-right-in-sql/

http://blog.forcerank.it/sql-for-calculating-churn-retention-reengagement

<https://catchjs.com/Blog/Churn>. churn rate

https://news.ycombinator.com/item?id=24831637

<https://habr.com/ru/post/496750/> stratification

<https://habr.com/ru/company/yandex/blog/497804/>  stratification

<https://www.khanacademy.org/math/ap-statistics/tests-significance-ap/one-sample-t-test-mean/v/calculating-p-value-from-t-statistic>

### Looker

<https://kickstarter.engineering/a-b-test-reporting-in-looker-bf4869f6b52>

<https://discourse.looker.com/t/simplified-a-b-test-analysis-redshift-python-udf-and-p-value-measure/2635>


###  degrees of freedom
Degrees of freedom are a measure the amount of variability involved in the research, which is determined by the number of categories you are examining. The equation for degrees of freedom is Degrees of freedom = n-1, where "n" is the number of categories or variables being analyzed in your experiment.

### t-statistic: 
represents the difference between averages of test and control group in units of standard error. Higher t-statistic value means bigger difference and supports our hypothesis.

<https://en.wikipedia.org/wiki/T-statistic>

### p-value: 
measures the probability of the null hypothesis to be true.

<https://www.wikihow.com/Calculate-P-Value>

<https://en.wikipedia.org/wiki/P-value>

### significance level (a)

### statistical power (1-b)


<https://towardsdatascience.com/the-ultimate-guide-to-a-b-testing-part-3-parametric-tests-2c629e8d98f8>

<https://towardsdatascience.com/the-ultimate-guide-to-a-b-testing-part-4-non-parametric-tests-4db7b4b6a974>

## Student’s T-distribution

https://habr.com/ru/post/559062/

T-distribution is a cousin of the Normal distribution - a bit shorter and fatter .
The T-distribution is used instead of the normal distribution when you have small samples (usually in practice less than 30). The larger the size of your sample, the more the t-distribution looks like the normal one.  

# Chi-Square distribution

<https://www.udemy.com/tutorial/statistics-by-example/feel-the-chi-square-statistic/>

<https://study.com/academy/lesson/the-chi-square-test.html>

  This one is widely used for statistical testing of categorical data.
Chi-square distribution is a special case of gamma-distribution (just like T-distribution), and has only one parameter: degrees of freedom (ν), which is as simple as number of possible categories minus one. The distribution only has positive values, and it is right-screwed. Its shape varies depending on ν: from very asymmetric with low ν, to almost normally-shaped with very high ν (with ν approaches infinity, chi-square distribution becomes normal distribution)

## Online calcs

<https://www.danielsoper.com/statcalc/default.aspx#c14>

<https://www.evanmiller.org/ab-testing/>

<https://vwo.com/tools/ab-test-siginficance-calculator/>

A typical 95% confidence level for an A/B test corresponds to a significance level of 0.05.
```
        | Converted | Total visits | Conversion Rate
--------|-------------------------------------------
Control | Cn        | Ct           |  Cn / Ct
Variant | Vn        | Vt           |  Vn / Vt
```

Lift = diff between Conversion rates
 We can assume that the distribution for our control group is binomial because the data is a series of Bernoulli trials, where each trial only has two possible outcomes (similar to a coin flip).
 Intuitively, we would feel more confident in our results as our sample sizes grow larger.  
 
Null hypotesis: Conversion rates are the same
## Code (SQL)

### z-score = (x - μ / σ)

https://hakibenita.com/sql-anomaly-detection

<http://www.silota.com/docs/recipes/sql-z-score.html>

z-score for a set of values by subtracting the average
 from the value and dividing the result by the standard deviation.
```
select  (a - avg(a)) / stddev(a) as z-score
```
```
 select  col_a - avg(a) over()) / stdev(a) over() 
```    

Postgres window function:
```
SELECT v, (v - (AVG(v) OVER ()) / (stddev(v) OVER ())) AS z_v
FROM  (
VALUES (1),(2),(3)
) vals (v);
```

```
with sales_stats as
    (select avg(sales) as mean,
            stddev(sales) as sd
    from zscore),
    visitor_stats as
    (select avg(visitors) as mean,
            stddev(visitors) as sd
    from zscore)
select dt,
    abs(sales - sales_stats.mean) / sales_stats.sd as z_score_sales,
    abs(visitors - visitor_stats.mean) / visitor_stats.sd as z_score_visitors
from sales_stats,
    visitor_stats,
    zscore;
```    

## Redshift + python
<http://michaelerasm.us/post/a-redshift-udf-to-find-ab-test-significance/>

<https://engineering.ezcater.com/measuring-ab-tests-sql-for-pvalue-graphs-in-redshift>

<https://www.sisense.com/blog/ab-testing-in-redshift/>

<http://michaelerasm.us/post/window-functions-in-redshift/> 

## Code (python)

<https://www.quora.com/How-can-I-do-an-A-B-test-in-Python>

<https://stats.stackexchange.com/questions/329465/assessing-a-b-test-results-using-python>

<https://towardsdatascience.com/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f>

<https://www.mikulskibartosz.name/how-to-perform-an-ab-test-correctly-in-python/>

<https://towardsdatascience.com/a-b-testing-design-execution-6cf9e27c6559>

<https://medium.com/@sasidhar.konda/ab-testing-in-python-1b5608207d86>

<https://medium.com/@henryfeng/handy-functions-for-a-b-testing-in-python-f6fdff892a90>


## Online Classes

<https://www.udacity.com/course/ab-testing--ud257> free course

<https://www.datacamp.com/courses/customer-analytics-ab-testing-in-python> . free course

<https://towardsdatascience.com/a-summary-of-udacity-a-b-testing-course-9ecc32dedbb1>


## CTR, Page View
<https://en.wikipedia.org/wiki/Click-through_rate>

the percentage of people visiting a web page who access a hypertext link to a particular advertisement.

The Click-through-probability (CTP) is the probability a given user clicks to get to the next step.

<https://www.digitalpacific.com.au/blog/what-is-the-difference-between-hits-visits-unique-visitors-page-impressions/>

Конверсия вычисляется как доля от общего числа посетителей, совершивших какое-либо действие. Действием может быть заполнение формы на посадочной странице, совершение покупки в интернет-магазине, регистрация, подписка на новости, клик на ссылку или блок.

A pageview or page view, abbreviated in business to PV and occasionally called page impression, is a request to load a single HTML file (web page) of an Internet site.[1] 

Т-критерий Стюдента требует нормальное распределение. Вы предлагаете биномиальное (конверсия). Нормальная аппроксимация справедлива когда pn>5 и n(1-p)>5. en.wikipedia.org/wiki/Binomial_proportion_confidence_interval

Т.е. если на сайте 1% конверсии, то выборка должна быть на 500 кликов минимум. Если мы изучаем клики по банеру c CTR 0.1%, то показов должно быть 5к минимум. Так что не совсем верно: «Этот тест хорошо зарекомендовал себя для небольших объемов данных».



### Hive from Python

<https://stackoverflow.com/questions/21370431/how-to-access-hive-via-python>

<https://towardsdatascience.com/working-with-hive-using-aws-s3-and-python-4c7471533f98>



<https://habr.com/ru/search/?q=%5Bab%20testing%5D&target_type=posts>


<https://tech.showmax.com/2020/02/ab-testing-part1/> 

<https://en.wikipedia.org/wiki/A/B_testing>

<https://towardsdatascience.com/a-collection-of-a-b-testing-learning-resources-newbie-to-master-6bab1e0d7845>

<https://datasketches.apache.org/docs/Theta/ThetaSketchFramework.html>

UDF for Hive (Java)
<https://github.com/rexrliu/hiveudf/blob/master/src/main/java/com/hive/udf/TTest.java>

* What are we trying to test and what metrics to use?
* How to estimate the sample size and pick confidence & power level prior to the test (FYI here is the link to Adobe Target’s sample size calculator)?
* How to split the test audience?
* What statistical test to use to calculate the significance level (assuming a traditional t-test is what’s considered here)?
* How long to run the tests for?
* How to interpret the results and make decisions accordingly?


The metrics we choose for sanity check are called as invariant metrics. They are not supposed to be affected by the experiment. They should not change across control and treatment groups. Otherwise, the experiment setup is incorrect.

<https://www.discoverdev.io/tags/ab-testing>



## A/A testing

Test Auditing (e.g. A/A Tests)
After setting up a new launch surface or new testing software for the first time, it’s important to validate the testing pipeline (data collection, user assignment, behavior tracking); otherwise, invalid results are not only a waste of time but also prone to wrong business decisions, if not investigated thoroughly. Section 8 in the “Seven Pitfalls to Avoid when Running Controlled Experiments on the Web” paper gives a comprehensive list of methods for validating the testing pipeline, including online/offline A/A tests, instrumentation, etc.).

http://ai.stanford.edu/people/ronnyk/2009-ExPpitfalls.pdf

<https://vwo.com/ab-testing/>

<https://tactics.convertize.com/> . 250 Best A/B Testing Ideas Based On Neuromarketing

<https://www.hbs.edu/faculty/Publication%20Files/20-018_e5cf26cb-b370-43b2-81c4-96a83066bf13.pdf>



##  A/B testing

<https://zulily-tech.com/2019/10/11/the-power-of-a-b-testing/>

<https://zulily-tech.com/2018/04/06/practical-a-b-testing/>

<https://www.periscopedata.com/blog/a-b-test-reporting-and-visualization-in-sql>

<https://habr.com/ru/company/otus/blog/481936/>

## Multi-armed bandit

https://habr.com/ru/company/domclick/blog/547258/ 

https://visualstudiomagazine.com/articles/2019/06/01/thompson-sampling.aspx   How to Do Thompson Sampling Using Python

<https://en.wikipedia.org/wiki/Multi-armed_bandit>   Multi-armed bandit

https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html

https://www.youtube.com/watch?v=yQwJiFFIgjA

https://en.wikipedia.org/wiki/Thompson_sampling

https://arxiv.org/pdf/1707.02038.pdf A Tutorial on Thompson Sampling

https://towardsdatascience.com/multi-armed-bandits-thompson-sampling-algorithm-fea205cf31df 

https://towardsdatascience.com/solving-multiarmed-bandits-a-comparison-of-epsilon-greedy-and-thompson-sampling-d97167ca9a50

https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf

https://medium.com/analytics-vidhya/multi-armed-bandit-analysis-of-thompson-sampling-algorithm-6375271f40d1

https://towardsdatascience.com/hompson-sampling-for-multi-armed-bandit-problems-part-1-b750cbbdad34

https://habr.com/ru/company/mailru/blog/539176/



<https://www.optimizely.com/optimization-glossary/multi-armed-bandit/>

<https://towardsdatascience.com/beyond-a-b-testing-multi-armed-bandit-experiments-1493f709f804>

<https://engineering.linkedin.com/blog/2020/making-the-linkedin-experimentation-engine-20x-faster>  LinkedIn framework


## Netflix, Linkedin, etc

<https://engineering.linkedin.com/blog/topic/ab-testing>

<https://medium.com/netflix-techblog/reimagining-experimentation-analysis-at-netflix-71356393af21>

<https://medium.com/netflix-techblog/its-all-a-bout-testing-the-netflix-experimentation-platform-4e1ca458c15>

<https://betatesting.com/blog/2018/02/23/how-netflix-does-ab-testing/>

<https://martechtoday.com/how-netflix-quasi-experiments-let-it-go-beyond-the-limitations-of-a-b-testing-231882>

<https://medium.com/netflix-techblog/tagged/experimentation>
