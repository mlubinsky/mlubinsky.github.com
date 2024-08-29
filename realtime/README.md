https://habr.com/ru/company/southbridge/blog/716022/. Kafka, BigQuery & Looker Studio

https://vutr.substack.com/p/how-did-facebook-design-their-real

https://habr.com/ru/companies/southbridge/articles/731526/ Streaming

https://habr.com/ru/companies/southbridge/articles/730380/

https://habr.com/ru/companies/uchi_ru/articles/730330/

https://towardsdatascience.com/real-time-event-streaming-with-kafka-bigquery-69c3baebb51e

```
Examples with python
Мы будем использовать пакет Faker для создания поддельных потоковых данных для нашего приложения. Наша поддельная полезная нагрузка события будет выглядеть примерно так:

{'user_id':001,
'artist': 'tony-allen',
'song_id': 03, 
'song_name':  'lady',
'event_type':'song_completed',
'timestamp': '2022-11-03 07:22:13'}
Чтобы установить пакет Faker, запустите это в окне терминала:

pip install Faker
```


https://fennel.ai/blog/challenges-of-building-realtime-ml-pipelines/

https://itnext.io/exploring-popular-open-source-stream-processing-technologies-part-2-of-2-2832b7727cd0

https://www.youtube.com/watch?v=wBd2TN4BP8A PART 1 - Introduction to real-time machine learning prediction demo

https://redpanda.com/blog/data-stream-processing-spark-flink-ksqldb

https://www.bytewax.io/blog/stream-processing-roundup

https://www.bytewax.io/blog/stream-processing-roundup2

### Pinot and Flink
https://www.youtube.com/watch?v=0byVuWrwOhw

### Pinot
https://dev.startree.ai/

https://www.youtube.com/watch?v=GvVYG6chYoI Druid / Pinot

Eaach table in Pinot is associated with a Schema. 
A schema defines what fields are present in the table along with the data types. 
The schema is stored in Zookeeper, along with the table configuration.

Below, we see the schema and config for one of the three Realtime tables, purchasesEnriched. 
Note how the columns are divided into three categories:
-  Dimension
-  Metric
-  DateTime


 


### How to stream data from database to web, as soon as they are inserted into a table.

https://petrjahoda.medium.com/stream-data-from-postgres-to-web-using-go-backend-bd7d7527fe27

https://materialize.com/a-simple-and-efficient-real-time-application-powered-by-materializes-tail-command/


### GnuPlot

https://habr.com/ru/post/546956/

<https://habr.com/ru/company/ruvds/blog/517450/>

<https://cyberchris.xyz/posts/awk-and-gnuplot/>


###  Small application that plots lines that are sent to the application's stdin

 https://branc116.github.io/brplot/
 
 https://github.com/branc116/brplot

### Bokeh

https://habr.com/ru/company/skillfactory/blog/526076/



### Plotly
<https://habr.com/ru/company/skillfactory/blog/506974/>

<https://medium.com/plotly/interactive-and-scalable-dashboards-with-vaex-and-dash-9b104b2dc9f0>

How We Created a Realtime Patient Monitoring System With Go and Vue in 3 days
<https://kasvith.me/posts/how-we-created-a-realtime-patient-monitoring-system-with-go-and-vue/>
<https://news.ycombinator.com/item?id=23051242>

<https://habr.com/ru/post/478750/> React and non-react plotting

<https://css-tricks.com/the-many-ways-of-getting-data-into-charts/>

<https://www.freecodecamp.org/news/5-ways-to-build-real-time-apps-with-javascript-5f4d8fe259f7/>

<https://engineering.instawork.com/real-time-web-apps-with-zero-lines-of-js-d2a3d6dd10d>

<https://news.ycombinator.com/item?id=20887708> d3.js

1. Long-Polling: This is the net equivalent of kids asking “are we there yet?” every five minutes
```
(function poll(){   
      setTimeout(function(){      
                            $.ajax({ url: "server", success: function(data){        
                               //Update your dashboard gauge        
                               salesGauge.setValue(data.value);
                               //Setup the next poll recursively        
                               poll();      }, 
                           dataType: "json"});  }, 30000);})();
```
## Web Socket


<https://www.ably.io/blog/websockets-vs-sse/>

Websockets and SSE (Server Sent Events) are both capable of pushing data to browsers, however they are not competing technologies. 

Websockets connections can both send data to the browser and receive data from the browser. A good example of an application that could use websockets is a chat application.

<https://blog.easyaspy.org/post/10/2019-04-30-creating-real-time-charts-with-flask>

<https://redstapler.co/javascript-realtime-chart-plotly/>

<https://stackoverflow.com/questions/5195452/websockets-vs-server-sent-events-eventsource>

<https://github.com/duyetdev/realtime-dashboard>

<https://developer.ibm.com/tutorials/realtime-visitor-analysis-with-kafka/>

## SSE is part of the browser EventSource API
<https://www.ably.io/concepts/server-sent-events>

<https://en.wikipedia.org/wiki/Server-sent_events>

<https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events>

text/event-stream is the official media type for Server Sent Events (SSE); it will prefix data bits with a data: prefix and you can also choose your prefix to change the meaning of that piece of data for the client. This media type is for browsers, as they support that using the EventSource JavaScript API.

application/stream+json is for server to server/http client (anything that's not a browser) communications. It won't prefix the data and will just use CRLF to split the pieces of data. 
<https://hpbn.co/server-sent-events-sse/>

<https://www.w3schools.com/html/html5_serversentevents.asp>

<https://www.smashingmagazine.com/2018/02/sse-websockets-data-flow-http2/>
<https://github.com/mchaov/simple-sse-nodejs-setup/blob/master/server.js>

Each EventSource object has the following members:
```
URL: set during construction.
Request: initially is null.
Reconnection time: value in ms (user-agent-defined value).
Last event ID: initially an empty string.
Ready state: state of the connection.
    CONNECTING (0)
    OPEN (1)
    CLOSED (2)
Apart from the URL, all are treated like private and cannot be accessed from outside.

Build-in events:

Open
Message
Error
```

```
    // subscribe for messages
    var source = new EventSource('URL');

    // handle messages
    source.onmessage = function(event) {
        // Do something with the data:
        event.data;
    };
```
Note that below in server code you don’t see a send() or push() method call. 
This is because the standard defines that 
the message is going to be sent as soon as it receives two \n\n characters 
as in the example: response.write("data: " + data + '\n\n');. 
This will immediately push the message to the client. 
Please note that the data must be an escaped string and doesn’t have new line characters at the end of it.
```
function handler(response)
    {
        // setup headers for the response in order to get the persistent HTTP connection
        response.writeHead(200, {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive'
        });

        // compose the message
        response.write('id: UniqueID\n');
        response.write("data: " + data + '\n\n'); 
        // whenever you send two new line characters the message is sent automatically
    }
```
Server-sent events (SSE) is a technology where a browser receives automatic updates from a server via HTTP connection
(standardized in HTML5 standards). 

Kafka doesn’t natively support this protocol, so we need to add an additional service to make this happen.

<https://hackernoon.com/supercharging-kafka-enable-realtime-web-streaming-by-adding-pushpin-fd62a9809d94>

## Kafka WebSocket
<https://www.confluent.io/blog/consuming-messages-out-of-apache-kafka-in-a-browser>

## Mosquitto  
$ mosquitto -c /path/to/mosquitto.conf
port 1883

listener 1884
protocol websockets

client = new Paho.MQTT.Client("localhost", 1883, "myclientid_" + parseInt(Math.random() * 100, 10));

## MQTT Websocket  

https://www.eclipse.org/paho/clients/js/

https://www.cloudmqtt.com/docs-websocket.html

<https://www.cumulocity.com/guides/mqtt/hello-mqtt-javascript/>

https://gist.github.com/matbor/9825309

http://www.astracorp.com/blog/mqtt-over-websockets

https://stackoverflow.com/questions/30624897/direct-mqtt-vs-mqtt-over-websocket

http://www.steves-internet-guide.com/mqtt-websockets/

http://www.steves-internet-guide.com/using-javascript-mqtt-client-websockets/

http://www.steves-internet-guide.com/wp-content/uploads/javascript-websockets.7z

https://github.com/mqttjs/MQTT.js

https://jpmens.net/2014/07/03/the-mosquitto-mqtt-broker-gets-websockets-support/

## MQTT plotting

<https://www.ably.io/concepts/mqtt>  MQTT overview

<https://tinker.yeoman.com.au/2015/05/11/simple-browser-based-graphical-display-of-mqtt-data/>

<http://www.mqtt-dashboard.com/metrics.html>




## HighCharts

<https://www.npmjs.com/package/highcharts>

https://tech.scargill.net/node-red-and-highcharts/

https://medium.com/@chakrar27/mqtt-highcharts-a-powerful-combo-for-building-real-time-dashboards-2d97880ee01d

https://github.com/matbor/mqtt2highcharts

https://gist.github.com/vitormeriat/b6de7aa0a28af2b45f15c3d67721e051


### SVG

<https://css-tricks.com/accessible-svgs/%3C/svg>

<https://able.bio/dbmzzo/intro-to-svg-for-react-developers--56cmmcy>

## Canvas vs SVG implementation
<https://habr.com/ru/company/ruvds/blog/476292/>

SVG is way slower than canvas though
Advantage SVG: if you want to do some advanced interactivity. That can sometimes be easier in SVG.

## Chart.js

<https://github.com/IridiumIO/pyChart.js>

<https://news.ycombinator.com/item?id=21170288>

<https://www.stanleyulili.com/javascript/beginner-guide-to-chartjs/>

<https://github.com/chartjs/awesome>

<https://github.com/nagix/chartjs-plugin-streaming> real time plugin



## JS plotting libraries

<https://blog.bitsrc.io/11-javascript-charts-and-data-visualization-libraries-for-2018-f01a283a5727>

<https://echarts.apache.org> 

<https://nivo.rocks/> .  React components on top of d3.

<https://deck.gl/> WebGL-powered framework for visual exploratory data analysis of large datasets.

<https://github.com/leeoniya/uPlot>  Time series charting library

<https://github.com/jwilber/roughViz>

<https://github.com/apexcharts/apexcharts.js>

<https://selleo.com/blog/javascript-data-visualization-libraries-comparison-table>

<https://www.codewall.co.uk/the-best-javascript-data-visualization-charting-libraries/>

<https://blog.bitsrc.io/11-javascript-charts-and-data-visualization-libraries-for-2018-f01a283a5727>

<https://habr.com/company/ruvds/blog/423983/>

<https://frappe.io/charts>

<https://medium.com/better-programming/modern-and-simple-charts-with-frappe-charts-c1b16244f8c>

## React plotting

<https://cube.dev/blog/react-visualization-libraries-in-2019/>

## Real-time plotting

<https://itnext.io/javascript-real-time-visualization-of-high-frequency-streams-d6533c774794>

<https://pusher.com/tutorials/live-graph-d3>

<https://github.com/hasura/graphql-engine/tree/master/community/tools/graphql2chartjs>

<https://itnext.io/javascript-real-time-visualization-of-high-frequency-streams-d6533c774794>

<https://medium.com/@xaviergeerinck/building-a-real-time-streaming-dashboard-with-spark-grafana-chronograf-and-influxdb-e262b68087de>
