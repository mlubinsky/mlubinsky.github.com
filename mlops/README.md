https://www.evidentlyai.com/ml-system-design

https://habr.com/ru/companies/beeline_tech/articles/760308/

https://www.hopsworks.ai/mlops-dictionary

https://habr.com/ru/companies/otus/articles/735170/

https://habr.com/ru/articles/743782/

https://habr.com/ru/company/selectel/blog/703460/

https://habr.com/ru/companies/skbkontur/articles/729068/

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
