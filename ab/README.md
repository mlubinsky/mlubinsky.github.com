



## Online calcs

<https://www.evanmiller.org/ab-testing/>

<https://vwo.com/tools/ab-test-siginficance-calculator/>

## Code (python)

<https://towardsdatascience.com/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f>

<https://www.mikulskibartosz.name/how-to-perform-an-ab-test-correctly-in-python/>

<https://towardsdatascience.com/a-b-testing-design-execution-6cf9e27c6559>

<https://medium.com/@sasidhar.konda/ab-testing-in-python-1b5608207d86>

<https://medium.com/@henryfeng/handy-functions-for-a-b-testing-in-python-f6fdff892a90>


## Online Classes

<https://www.udacity.com/course/ab-testing--ud257> free course

<https://www.datacamp.com/courses/customer-analytics-ab-testing-in-python> . free course

<https://towardsdatascience.com/a-summary-of-udacity-a-b-testing-course-9ecc32dedbb1>


## CTR
<https://en.wikipedia.org/wiki/Click-through_rate>

the percentage of people visiting a web page who access a hypertext link to a particular advertisement.

The Click-through-probability (CTP) is the probability a given user clicks to get to the next step.


Конверсия вычисляется как доля от общего числа посетителей, совершивших какое-либо действие. Действием может быть заполнение формы на посадочной странице, совершение покупки в интернет-магазине, регистрация, подписка на новости, клик на ссылку или блок.

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

<https://en.wikipedia.org/wiki/Multi-armed_bandit>   Multi-armed bandit

<https://www.optimizely.com/optimization-glossary/multi-armed-bandit/>

<https://towardsdatascience.com/beyond-a-b-testing-multi-armed-bandit-experiments-1493f709f804>

<https://engineering.linkedin.com/blog/2020/making-the-linkedin-experimentation-engine-20x-faster>  LinkedIn framework

<https://discourse.looker.com/t/simplified-a-b-test-analysis-redshift-python-udf-and-p-value-measure/2635>

## Netflix, Linkedin, etc

<https://engineering.linkedin.com/blog/topic/ab-testing>

<https://medium.com/netflix-techblog/reimagining-experimentation-analysis-at-netflix-71356393af21>

<https://medium.com/netflix-techblog/its-all-a-bout-testing-the-netflix-experimentation-platform-4e1ca458c15>

<https://betatesting.com/blog/2018/02/23/how-netflix-does-ab-testing/>

<https://martechtoday.com/how-netflix-quasi-experiments-let-it-go-beyond-the-limitations-of-a-b-testing-231882>

<https://medium.com/netflix-techblog/tagged/experimentation>
