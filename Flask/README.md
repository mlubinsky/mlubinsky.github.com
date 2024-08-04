Pyotr is a Python library for serving and consuming REST APIs based on OpenAPI specifications. Its name is acronym of "Python OpenAPI to REST".

https://pyotr.readthedocs.io/en/latest/

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
   
