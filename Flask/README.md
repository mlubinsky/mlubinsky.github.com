### Flask console output
```
The lines you’re seeing are Flask’s built-in logging for incoming requests, which is handled by the werkzeug library.
These logs appear every time your Flask server handles a request, in this case, showing an HTTP DELETE request.

To suppress these logs, you can adjust the log level or disable them entirely:

Option 1:
Set the Log Level to Higher than INFO
If you still want to keep error logs but ignore regular request logs, you can set the Flask log level to a higher level like WARNING or ERROR.

 
import logging
import werkzeug
werkzeug.logger.setLevel(logging.WARNING)

Option 2: Run Flask in Production Mode
If you’re running Flask in development mode, werkzeug will log requests by default.
Running in production mode (e.g., with a production server like gunicorn) will suppress these logs by default:

 
export FLASK_ENV=production
flask run

Option 3: Disable the Access Log in the Flask Embedded Server
If you only want to disable the access log without changing the log level, try:

 
from flask import Flask
import logging

app = Flask(__name__)

# Disable Werkzeug request logging
log = logging.getLogger('werkzeug')
log.disabled = True

```

 
### Flask issues
```
The fact that refreshing your browser (making a GET request) allows the POST request from your Python program to work suggests that there might be a few underlying issues that involve network behavior, threading in Flask’s development server, or a blocking operation. Here are some possible causes and solutions:

Possible Causes and Solutions:
1. Flask Development Server is Single-Threaded:
The Flask development server is single-threaded by default. If the GET request keeps the server alive by opening a new thread or connection, it may prevent the POST request from hanging.
Solution: Enable multi-threading in Flask by setting the threaded=True option in app.run(). This allows the server to handle multiple requests concurrently.
Modify your app.run() function like this:
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True)
This will enable Flask to handle multiple requests (both GET and POST) without blocking each other.

2. Blocking Operation in Flask Route:
If the POST request handler involves any blocking operation (e.g., waiting for a resource, file operations, etc.), it could be stalling the request, especially in a single-threaded server.
Solution: Review the logic inside your POST route handler to ensure there are no blocking operations. You might need to use asynchronous processing (via asyncio, background threads, or queues) for long-running tasks.


3. Network or Localhost Issues:
It's possible that there are issues with how localhost or 127.0.0.1 is being resolved or handled on your machine. The browser request could be "warming up" the connection or resetting some network condition.
Solution: Try using localhost, 127.0.0.1, or your local IP address interchangeably. Sometimes switching between these can resolve issues with local networking. For example, replace 127.0.0.1 with localhost in your Python client:
 
url = 'http://localhost:5000/tasks'


4. Browser Caching or Keep-Alive Behavior:
Web browsers often reuse connections with the Flask server and keep the connection alive. This might be why a browser refresh helps the POST request go through, as it reopens the connection or keeps it from being closed abruptly.
Solution: Ensure that your Python client also uses persistent connections by setting the Connection: keep-alive header. Here's how you can modify your requests.post() call:
 
headers = {'Connection': 'keep-alive'}
response = requests.post(url, json=data, headers=headers, timeout=10)


5. Debugging with Logs:
Review the Flask logs to see if there are any clues about what happens when the POST request is made. You can also enable more verbose logging in Flask:
 
import logging
logging.basicConfig(level=logging.DEBUG)


6. Concurrent Requests Handling:
If you're experiencing connection issues when Flask tries to handle multiple requests at once (for example, one GET and one POST), this might indicate an issue with how Flask handles concurrency in its development server.
Solution: Consider running your Flask app with a more robust server like Waitress or Gunicorn, which can handle multiple concurrent requests more efficiently.
To install Waitress:

 
pip install waitress
Run your Flask app with Waitress:

from waitress import serve
from your_flask_app import app

serve(app, host='0.0.0.0', port=5000)
Debugging Steps:
Check Flask Logs: Monitor the Flask server logs for any errors or warnings when the POST request is made.

Enable Multi-threading: Ensure that the server is running with threaded=True to support concurrent requests.

Test localhost vs 127.0.0.1: Try using localhost or your machine's IP instead of 127.0.0.1 to see if there’s any change in behavior.

Use Persistent Connections: Set the Connection: keep-alive header in your Python client to ensure the connection isn’t prematurely closed.

By enabling multi-threading and ensuring proper network connection handling, the issue may resolve itself. Let me know how this works or if you encounter further challenges!








```

Pyotr is a Python library for serving and consuming REST APIs based on OpenAPI specifications. Its name is acronym of "Python OpenAPI to REST".

https://pyotr.readthedocs.io/en/latest/

https://talkpython.fm/episodes/show/472/state-of-flask-and-pallets-in-2024  State of Flask in 2024

https://testdriven.io/blog/flask-htmx-tailwind/  HTMX

https://habr.com/ru/articles/833446/  Big Flask Project

<https://www.youtube.com/watch?v=TG8xZV5YCI4>

<https://habr.com/ru/post/497724/>

https://www.reddit.com/r/flask/comments/jxt71p/my_best_flask_projects_so_far/

<https://webargs.readthedocs.io/en/latest/>. WebArgs

<https://justpy.io/#/>  high-level Python Web Framework that requires no front-end programming. With a few lines of only Python code, you can create interactive websites without any JavaScript programming.

<https://docs.streamlit.io/> . Streamlit is an open-source Python library that makes it easy to build beautiful apps for machine learning.

<https://github.com/man-group/dtale> . Flask/React client for visualizing pandas data structures 

### Redis Celery Flask

<https://ljvmiranda921.github.io/notebook/2019/11/08/flask-redis-celery-mcdo/>

<https://news.ycombinator.com/item?id=22901856>



####  Flask and KAfka
https://medium.com/geekculture/streaming-model-inference-using-flask-and-kafka-3476d9ff5ca5

## Flask

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

https://habr.com/ru/articles/804245/

<https://unix.stackexchange.com/questions/182537/write-python-stdout-to-file-immediately>

<https://stackoverflow.com/questions/38630421/how-to-execute-shell-command-and-stream-output-with-python-and-flask-upon-http-r>

<https://stackoverflow.com/questions/35540885/display-the-contents-of-a-log-file-as-it-is-updated>

app.py
```
@app.route('/stream')
def stream():
    def generate():
        fname="/Users/miclub01/tmp/job.log"
        with open(fname) as f:
            while True:
                yield f.read()
                sleep(1)
    print("generate=", generate());
    return app.response_class(generate(), mimetype='text/plain')

app.run()
```

cat  templates/index.html
```

<pre id="output"></pre>
<script>
    var output = document.getElementById('output');
    console.log("step 1")
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '{{ url_for('stream') }}');
    xhr.send();
    console.log("step 5")

    setInterval(function() {
        output.textContent = xhr.responseText;
        // console.log( "**" + output.textContent );
    }, 1000);
</script>
```

python write2log.py >> ~/tmp/job.log

cat write2log.py
```
import time

i=0
while True:
  i += 1
  time.sleep( 2 )
  print(str(i) , flush=True)  # Python3 only flag
```  

<https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running/28319191#28319191>

<https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running>

<https://www.youtube.com/watch?v=gJ7CnUX_7YQ> Async Flask




<https://blog.easyaspy.org/post/1/2018-12-28-how-i-created-easyaspy-from-scratch-using-flask>

<https://github.com/apryor6/flask_api_example>

<https://testdriven.io/courses/tdd-flask/>  Developing a RESTful API with Python, Flask, Docker, and Pytest


<https://youtu.be/e-_tsR0hVLQ> Flask

## Admin Panel 
<https://habr.com/ru/post/477126/>  Flask + ReactAmin

<https://github.com/flask-admin/flask-admin>

<https://github.com/app-generator/flask-dashboard-adminlte>

https://github.com/app-generator/flask-dashboard-dattaable

## Fast API 

<https://fastapi.tiangolo.com/>

https://habr.com/ru/companies/amvera/articles/833588/

```
Сервис WebSim,   сгенерирует для нас фронтенд.
Подробное описание этого бесплатного сервиса и то, как им пользоваться
в этой статье: «WebSim AI: Бесплатный ИИ-помощник для быстрой веб-разработки»

Библиотеку CurlFetch2Py, которая будет выполнять основную логику нашего приложения. Подробное описание библиотеки и того какие она проблемы решает - тут:
«CurlFetch2Py –
Эффективное преобразование CURL и FETCH команд в структурированные Python объекты»


```

<https://habr.com/ru/post/478620/>

<http://www.uvicorn.org/>

https://news.ycombinator.com/item?id=25990702


### Django

https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html

https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html

https://news.ycombinator.com/item?id=27605052

https://habr.com/ru/post/456146/ .  +Vue

 


### Responder

https://training.talkpython.fm/courses/details/responder-web-framework-mini-course

### Flask

 
https://blog.appseed.us/flask-dashboard-open-source-and-free/ 
https://www.youtube.com/watch?v=zdgYw-3tzfI
https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33
https://habr.com/ru/post/448360/
https://www.reddit.com/r/flask/comments/2321oc/easiest_and_fastest_way_to_host_flask_python/

https://www.reddit.com/r/flask/comments/b4uoao/af_recommended_flask_video_tutorials_for_2019/

   

https://potion.readthedocs.io/en/latest/    Flask-Potion
https://habr.com/ru/post/472018/    Flask-Potion



https://www.roytuts.com/python-flask-file-upload-example/

 https://github.com/mlubinsky/mlubinsky.github.com/tree/master/Flask   My Flask code snippets</a>


### Shopping card  
https://www.google.com/search?q=shopping+card+REST+API++flask&oq=shopping+card+REST+API+flask
https://github.com/Durgaprasad-Nagarkatte/Simple-Flask-Shopping-Cart
http://blog.subair.net/simple-web-shop-cart-rest-api-python-3-and-flask/
https://github.com/lucassimon/flask-api-shopping-cart
https://github.com/HarshShah1997/Shopping-Cart
https://github.com/kkschick/ubermelon-shopping-app

### Async update Web page  
http://stackoverflow.com/questions/10377384/why-use-ajax-when-websockets-is-available

#### Option #1:

https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/
https://secdevops.ai/weekend-project-part-2-turning-flask-into-a-real-time-websocket-server-using-flask-socketio-ab6b45f1d896
Server-side events:
https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
http://datamining.city/2015/09/30/server-client-streaming/
http://flask.pocoo.org/snippets/116/

#### Option #2:

Flask + Ajax {via Polling}:   write a callback that will get called upon time out. 

This can be done, for instance, using JQuery's setInterval().

https://laracasts.com/discuss/channels/laravel/listen-to-new-event-and-refresh-page
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-ajax

### Udemy  
https://www.udemy.com/restful-api-flask-course/learn/v4/
https://www.udemy.com/rest-api-flask-and-python/learn/v4/content
https://www.udemy.com/es6-javascript-shopping-cart/learn/v4/overview


### Not Free 
 
https://testdriven.io/ - Microservices with Docker, Flask, and React
https://buildasaasappwithflask.com/
 

https://www.youtube.com/watch?v=EfgxnmOWLUE

## REST API 
 
https://blog.miguelgrinberg.com/category/Flask
https://habr.com/post/358152/  - Russian translation Flask REST API


 
https://www.reddit.com/r/flask/comments/9h5n17/what_are_the_best_resources_to_learn_flask/
https://www.reddit.com/r/flask/comments/8segyj/best_open_source_flask_repos_for_learning_design/
 
https://vsupalov.com/flask-megatutorial-review/
 

https://medium.com/search?q=flask
https://github.com/mjhea0/flaskr-tdd


https://praciano.com.br/blog/building-your-first-rest-application-with-python-and-flask-part-i/
https://realpython.com/flask-connexion-rest-api-part-2/

 
https://github.com/christabor/flask_jsondash
https://github.com/mjhea0/flaskr-tdd
https://lepture.com/en/2018/structure-of-a-flask-project

https://exploreflask.com/en/latest/index.html
https://github.com/realpython/discover-flask

Calling remote (async) API from Falsk usually requiire Celery

https://github.com/jpmens/mqttwarn MQT
https://github.com/pika/pika  Python RabbitMQ client
https://medium.freecodecamp.org/how-to-use-python-and-flask-to-build-a-web-app-an-in-depth-tutorial-437dbfe9f1c6


####  Deploying to Heroku and Pythonanyware 

https://pythonhow.com/deploying-your-web-application-to-the-cloud/ . Heroku

https://pythonhow.com/deploy-flask-web-app-pythonanywhere/

###  Deploying: AWS and Docker 
https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0

https://linuxacademy.com/blog/amazon-web-services-2/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/

## Deployment: AWS Docker
<https://www.codementor.io/@jqn/deploy-a-flask-app-on-aws-ec2-13hp1ilqy2> Flask + AWS EC2

<https://www.agiratech.com/debugging-python-flask-app-in-docker-container/> Flask in Docker

https://www.codementor.io/@mattthommes/trigger-local-python-app-remotely-117wunbuah . ngrok

https://www.reddit.com/r/flask/comments/ar4dsi/flaskuwsgi_app_and_docker/

https://medium.com/@jchaykow/productionalize-analytics-flask-app-with-docker-aws-and-google-api-bda5445949f6

How to make my flask server open to any device connected on my wifi?
If you have the debugger disabled or trust the users on your network,
you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

    flask run --host=0.0.0.0 
This tells your operating system to listen on all public IPs

if __name__=='__main__':
   app.run(debug=False, host='0.0.0.0', port=5000)
   
