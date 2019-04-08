Websockets and SSE (Server Sent Events) are both capable of pushing data to browsers, however they are not competing technologies. Websockets connections can both send data to the browser and receive data from the browser. A good example of an application that could use websockets is a chat application.

<https://redstapler.co/javascript-realtime-chart-plotly/>

<https://stackoverflow.com/questions/5195452/websockets-vs-server-sent-events-eventsource>

<https://github.com/duyetdev/realtime-dashboard>

<https://developer.ibm.com/tutorials/realtime-visitor-analysis-with-kafka/>

Server-sent events (SSE) is a technology where a browser receives automatic updates from a server via HTTP connection
(standardized in HTML5 standards). 

Kafka doesn’t natively support this protocol, so we need to add an additional service to make this happen.

<https://hackernoon.com/supercharging-kafka-enable-realtime-web-streaming-by-adding-pushpin-fd62a9809d94>
