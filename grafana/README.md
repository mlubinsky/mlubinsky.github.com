###  grafonnet - библиотека для написания дашбордов Grafana с помощью кода на языке jsonnet

https://habr.com/ru/company/mailru/blog/577230/

### Install Grafana  on Mac:
https://grafana.com/docs/grafana/latest/installation/mac/

https://grafana.com/docs/grafana/latest/getting-started/getting-started/

brew install grafana

To have launchd start Grafana now and restart at login:
```
brew services start grafana
```   
Or, if you don't want/need a background service you can just run:
```
  grafana-server --config=/usr/local/etc/grafana/grafana.ini --homepath /usr/local/share/grafana --packaging=brew cfg:default.paths.logs=/usr/local/var/log/grafana cfg:default.paths.data=/usr/local/var/lib/grafana cfg:default.paths.plugins=/usr/local/var/lib/grafana/plugins
```
http://localhost:3000/

Connecting to Prometeus: https://prometheus.io/docs/visualization/grafana/

## Prometheus

https://blog.pvincent.io/tags/prometheus/


https://habr.com/ru/company/timeweb/blog/562378/  PromQL

### Metric 
Metric is an identifier linking data points together over time. 
For example, the metric `http_requests_total` denotes all the data points collected by Prometheus 
for services exposing http requests counters
 
### Labels 

Labels are key-value pairs associated with time series that, in addition to the metric name, 
uniquely identify them.  

As there is likely to be multiple services exposing the same http_requests_total metric, 
labels can be added to each data point to specify which service this counter applies to:
```
# Request counter for the User Directory service
http_requests_total{service="users-directory"}

# Request counter for the Billing History Service
http_requests_total{service="billing-history"}

# Overall request counter regardless of service
sum(http_requests_total) 
```
### Install Prometheus
```
brew install prometheus
```
When run from `brew services`, `prometheus` is run from
`prometheus_brew_services` and uses the flags in:
   /usr/local/etc/prometheus.args

To have launchd start prometheus now and restart at login:
```
  brew services start prometheus
```  
Or, if you don't want/need a background service you can just run:
```
  prometheus --config.file=/usr/local/etc/prometheus.yml
```  


https://prometheus.io/docs/introduction/first_steps/

https://prometheus.io/download/

Node_exporter

https://github.com/prometheus/node_exporter/blob/master/README.md
```
  ./prometheus --config.file=prometheus.yml
  http://localhost:9090
  http://localhost:9090/metrics
  http://localhost:9090/graph
```

https://coralogix.com/blog/promql-tutorial-5-tricks-to-become-a-prometheus-god/

https://blog.pvincent.io/2017/12/prometheus-blog-series-part-1-metrics-and-labels/

### Show all available metrics:

Show all available metrics:

```
localhost:9090/api/v1/label/__name__/values
```
Data for the  specific metric name:

https://utils.us-east-1.mbedcloud.com/prometheus/api/v1/query?query=update_service_publisher_metrics


### VictoriaMetrics

<https://habr.com/ru/post/494034/>

<https://medium.com/@teebr/iot-with-an-esp32-influxdb-and-grafana-54abc9575fb2>>


<https://habr.com/ru/post/448676/>

<https://news.ycombinator.com/item?id=21343521>

<https://itnext.io/javascript-real-time-visualization-of-high-frequency-streams-d6533c774794>

<https://medium.com/@xaviergeerinck/building-a-real-time-streaming-dashboard-with-spark-grafana-chronograf-and-influxdb-e262b68087de>

https://github.com/creativetimofficial/material-dashboard

<https://grafana.com/docs/reference/templating/#the-timefilter-or-timefilter-variable>

https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019

https://habr.com/ru/post/482272/

 

<https://grafana.com/docs/reference/templating/#the-timefilter-or-timefilter-variable>

WHERE $__timeFilter  

<https://youtu.be/FhNUrueWwOk?list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2> . Variables in Grafana

<https://grafana.com/docs/reference/templating/>

<https://kb.groundworkopensource.com/display/DOC721/How+to+GroundWork+Grafana+dashboard+variables>

The templating feature allows you to create variables that can be used in your metric queries, series names and panel titles. Use this feature to create generic dashboards that can quickly be changed to show graphs for different servers or metrics.

https://github.com/ricardbejarano/graphql_exporter

http://localhost:3000/

http://localhost:3000/datasources

http://ec2-18-221-216-253.us-east-2.compute.amazonaws.com:3000/login . admin/admin1

<https://grafana.com/plugins/postgres>

http://docs.grafana.org/features/datasources/postgres/

https://grafana.com/blog/2018/10/15/make-time-series-exploration-easier-with-the-postgresql/timescaledb-query-editor/

https://stackoverflow.com/questions/48512014/using-postgres-with-grafana

https://habr.com/ru/company/1cloud/blog/443006/

https://www.youtube.com/watch?v=sKNZMtoSHN4&index=7&list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2


https://www.youtube.com/watch?v=sKNZMtoSHN4&index=7&list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2


## Prometheus - for system monitoring 


https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019

https://habr.com/ru/post/482272/

https://github.com/danielfm/prometheus-for-developers

https://habr.com/ru/company/southbridge/blog/455290/

 https://habr.com/ru/company/itsumma/blog/350200/
 
В состав Prometheus входят следующие компоненты:
* сервер, который считывает метрики и сохраняет их в темпоральной (time series) базе данных;
* клиентские библиотеки для различных языков программирования (Go, Java, Python, Ruby, ...)
* Pushgateway — компонент для приёма метрик кратковременных процессов;
* PROMDASH — дашборд для метрик;
* инструменты для экспорта данных из сторонних приложений (Statsd, Ganglia, HAProxy и других);
* менеджер уведомлений AlertManager (на текущий момент находится на стадии бета-тестирования);
* клиент командной строки для выполнения запросов к данным.

Большинство из них написаны на Go, а совсем небольшая часть — на Ruby и Java. 

Все компоненты Prometheus взаимодействуют между собой по протоколу HTTP:

Сбор метрик в Prometheus осуществляется с помощью механизма pull. 
Имеется также возможность сбора метрик с помощью механизма push (для этого используется специальный компонент pushgateway, 
который устанавливается отдельно). Это может понадобиться в ситуациях, 
когда сбор метрики с помощью pull по тем или иным причинам невозможен: например, при наблюдении за сервисами, защищёнными фаерволлом. Также механизм push может оказаться полезным при наблюдении за сервисами, 
подключающихся к сети периодически и на непродолжительное время.
 
Prometheus использует pull модель сбора метрик: у него есть список экспортеров и он опрашивает их по HTTP, 
собирая с них список метрик и кладя их к себе в хранилище.


Экспортер — это агент, который занимается сбором метрик непосредственно с сущности 
(сервера в целом, или конкретного приложения), которую надо мониторить. 
У Prometheus богатые возможности для инструментации, поэтому экспортеры есть для большинства популярных приложений, 
и написать свой в случае надобности не представляет особого труда.

https://habr.com/ru/post/345370/
postgres_exporter работает следующим образом: он подключается к PostgreSQL, выполняет запросы к служебным таблицам 
и выставляет результаты в специальном формате с помощью внутреннего HTTP-сервера для забора их Prometheus'ом. 
Важный момент: помимо большого набора дефолтных запросов, можно определить свои и собирать любые данные, 
которые можно получить с помощью SQL, включая какие-нибудь бизнес-метрики. 
 
https://habr.com/ru/company/selectel/blog/275803/
https://habr.com/ru/company/otus/blog/358588/

https://habr.com/ru/post/441136/ .  How to store metrics for a long time
https://habr.com/ru/company/funcorp/blog/445370/


Writing: Скорость накопления данных стремится к стабильной величине: обычно сервисы, которые вы мониторите, 
посылают примерно одинаковое количество метрик, и инфраструктура меняется относительно медленно. 

Integration with Grafana
https://grafana.com/dashboards/7901



https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019
https://habr.com/ru/post/482272/

https://github.com/danielfm/prometheus-for-developers
https://habr.com/ru/company/southbridge/blog/455290/
 
 
http://micrometer.io/ . JVM Application Monitoring
https://habr.com/ru/post/442080/

https://habr.com/ru/post/420633/ . GeoIP plotting (WorldMap)
https://habr.com/ru/post/412897/
