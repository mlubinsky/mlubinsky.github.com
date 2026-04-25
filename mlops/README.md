## ML Ops
https://mlip-cmu.github.io/book/

https://www.youtube.com/playlist?list=PLfFghEzKVmjttkxVtVIvNZRuoSUuWtsFN  Deploying ML

https://seattledataguy.substack.com/p/the-state-of-data-engineering-part-b61

https://github.com/graviraja/MLOps-Basics

https://www.evidentlyai.com/ml-system-design

https://habr.com/ru/companies/vk/articles/772538/

https://habr.com/ru/companies/otus/articles/773320/

https://habr.com/ru/companies/beeline_tech/articles/760308/

https://habr.com/ru/companies/beeline_tech/articles/760308/

https://www.hopsworks.ai/mlops-dictionary

https://habr.com/ru/companies/otus/articles/735170/

https://habr.com/ru/articles/743782/

https://habr.com/ru/company/selectel/blog/703460/

https://habr.com/ru/companies/skbkontur/articles/729068/

### MLFlow
https://mlflow.org/
```
Ключевые компоненты MLflow:

MLflow Tracking. Этот компонент позволяет вести логи и мониторинг экспериментов, фиксируя важные метрики, параметры и артефакты, связанные с разными runs.
MLflow Projects. «Проекты» позволяют упаковать спецификации кода, зависимостей и среды в формат, поддерживающий многократное использование. Это позволяет воспроизводить эксперименты, снижая вероятность нестыковок при переходе от разработки в продакшен.
MLflow Models. Это стандартный формат для упаковки моделей машинного обучения, который можно использовать в различных последующих инструментах, например для обслуживания в реальном времени через REST API или пакетного вывода в Apache Spark. Формат определяет соглашение, которое позволяет вам сохранять модель в разных «вариантах», которые могут быть поняты различными последующими инструментами.
MLflow Registry. Это хорошо организованная библиотека, в которой вы храните и управляете разными версиями обученных моделей машинного обучения. Нечто вроде полки с разными изданиями любимых книг. Model Registry в MLflow помогает отслеживать, как модели изменяются со временем; при этом в тот или иной момент можно легко найти и использовать нужную версию.

```
https://habr.com/ru/companies/vk/articles/770944/

https://codinginfinite.com/mlflow-tutorial-with-code-example/

https://docs.databricks.com/machine-learning/feature-store/index.html

 The raw data requires preprocessing and transformation before it can be used to build a model.
 This process is called feature engineering, and the outputs of this process are called features

https://kolodezev.ru/

https://arxiv.org/pdf/2205.02302.pdf

https://habr.com/ru/company/ruvds/blog/703164/

https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

https://habr.com/ru/company/ruvds/blog/703164/#:~:text=Machine%20learning%20operations%20(MLOps)

MLOps — это культура разработки ML, нацеленная на унификацию разработки (Dev) и эксплуатации (Ops) систем ML.

https://www.featurestore.org/


📕 MLOps books:
➡ Machine Learning Engineering with Python - Second Edition by Andy McMahon published by Packt
➡ Reliable Machine Learning: Applying SRE Principles to ML in Production by Cathy Chen, MA, CPCC, Niall Murphy, Kranti K. Parisa, D. Sculley, Todd Underwood

📰 MLOps and LLM(Ops) blogs:
➡ Chip Huyen: https://lnkd.in/gVB22DuE
➡ Eugene Yan: https://lnkd.in/gPwN8mSm
➡ Decoding ML by Paul Iusztin: https://lnkd.in/gQehWnHr
➡ LLM watch by Pascal Biese: https://lnkd.in/gJhZH4mb

📽 LLM(Ops) courses:
➡ Hands-on LLMs by Pau Labarta Bajo, Alexandru Răzvanț, and Paul Iusztin: https://lnkd.in/ggpxRsc7
➡ LLM BootCamp by Sergey Karayev, Charles Frye, and Josh Tobin: https://lnkd.in/gKMZGYSQ 
➡ Introduction to Q&A Systems with LLMs by Rahul Parundekar and MLOps Community: https://lnkd.in/gMYaFcTg

🔖 Curated lists of references for MLOps/LLM(Ops):
➡ Awesome LLMOps by Ce Gao: https://lnkd.in/gFrri858
➡ Awesome MLOps by Dr. Larysa Visengeriyeva: https://lnkd.in/eMttRFhA
➡ LLM roadmaps by Maxime Labonne: https://lnkd.in/dgpe7p4H

💡Together with Başak and Raphaël, we run Marvelous MLOps, where we share MLOps cheatsheets, memes, and articles on MLOps.
https://www.linkedin.com/company/marvelous-mlops/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BveUHM6moTAG6h3Yj6bnf2w%3D%3D

💡Check out my other recommendations on learning resources:
➡ Part 1: https://lnkd.in/gb36cyGG
➡ Part 2: https://lnkd.in/gYiXFDdD

### Feature engineering (конструирование признаков)
связано с автоматизацией конвейеров ETL и контролем их версий. В идеале это должно быть что-то в стиле feature store. Если вам незнакома эта концепция, то изучите этот веб-сайт. Некоторые из имеющихся на рынке инструментов: Databricks Feature Store, Feast, Tecton.

### Experiment tracking (учёт экспериментов) 
— крупный и по-настоящему критически важный компонент, потому что он связан с экспериментами инженеров ML (как с успешными, так и с неудачными). Когда настанет время, он позволяет вернуться к предыдущим идеям (например, к другим алгоритмам или признакам) без необходимости изобретать велосипед. В зрелой системе ML может также существовать способ сохранения набора гиперпараметров (прошлых и текущих), а также соответствующие KPI качества системы, обычно называемые реестром модели (инструменты наподобие MLflow, Neptune или Weight&Biases).

### Pipeline management (управление конвейерами) 
позволяет выполнять контроль версий конвейера, управляющего потоком данных от ввода до вывода. 
Также оно должно журналировать каждый прогон и выдавать осмысленные ошибки в случае возникновения проблем. 
Можно рассмотреть следующие инструменты: Vertex AI Pipelines, Kedro, PipelineX, Apache Airflow.
Compute management (управление вычислительными ресурсами) решает задачу масштабируемости в системах ML. 
Некоторые алгоритмы требуют огромных вычислительных мощностей при обучении и повторном обучении, но малых при вычислении результатов. 
Поскольку часто эти две задачи соединены цепью обратной связи, система должна уметь увеличивать и уменьшать свои масштабы. 
Иногда для обучения должны подключаться дополнительные ресурсы наподобие GPU, которые не требуются при вычислении результатов. 
Публичные поставщики облачных сервисов решают эту проблему, предоставляя функции автоматического масштабирования и балансировки нагрузки.

### Model CI/CD (CI/CD моделей) 
очень похожи на CI/CD из сферы DevOps, однако при развёртывании модели необходимо выполнять дополнительные проверки. 
Это выбранные метрики показателей, которые должны находиться в допустимом диапазоне и всегда сравниваться с текущей моделью в продакшене. 
Одни из самых популярных инструментов — Jenkins и Travis, но есть и множество других наподобие TeamCity или Circle CI.

### Drift detection (выявление дрейфа) — 
это модуль, отслеживающий характеристики входных данных и поведение системы.
Когда характеристики входных данных отклоняются от ожидаемого диапазона, должен выдаваться соответствующий алерт, 
чтобы можно было запросить повторное обучение системы (автоматическое или ручное). 
Если это не помогает, то приоритет алерта должен быть повышен, а команда разработчиков должна изучить проблему внимательнее. 
Инструменты/сервисы: AWS SageMaker Model Monitor, Arize, Evidently AI.
