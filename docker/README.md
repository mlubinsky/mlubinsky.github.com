```
Basic Interview Questions of Docker & Dockerfile:-

1. How will you run multiple Docker containers in one single host?
Answer: Docker Compose is the best way to run multiple containers as a single service by defining them in a docker-compose.yml file.

2. If you delete a running container, what happens to the data stored in that container?
Answer: When a running container is deleted, all data in its file system also goes away. However, we can use Docker Data Volumes to persist data even if the container is deleted.

3. How do you manage sensitive security data like passwords in Docker?
Answer: Docker Secrets and Docker Environment Variables can be used to manage sensitive data.

4. What is the difference between Docker Image and a Docker Container?
Answer: Docker Image is a template that contains the application, libraries, and dependencies required to run an application, whereas a Docker Container is the running instance of a Docker Image.

5. How do you handle persistent storage in Docker?
Answer: Docker Volumes and Docker Bind Mounts are used to handle persistent storage in Docker.

6. What is the process to create a Docker Container from a Dockerfile?
Answer: Docker Build command is used to create Docker images from a Dockerfile and then Docker Run command is used to create Containers from Docker images.

7. How will you scale Docker containers based on traffic to your application?
Answer: Docker Swarm or Kubernetes can be used to auto-scale Docker Containers based on traffic load.

8. When RUN and CMD instructions will be executed?
Answer: RUN instruction will be executed while building the Docker Image. CMD instruction will be executed while starting the Container.

9. What’s the different between COPY and ADD instructions?
Answer: Using COPY instruction,We can copy local files and folders from docker build context to Docker Image. These files and folders will be copied while creating a Docker Image.
ADD instruction works similar to COPY instruction but the only different is that we can download files from remote locations that’s from Internet while creating a Docker Image.

10. What’s the different between CMD and ENTRYPOINT instructions?
Answer: CMD instruction will be used to start the process or application inside the Container.
ENTRYPOINT instruction also works similar to CMD instruction. ENTRYPOINT instruction will also be executed while creating a container. CMD instruction can be overridden while creating a Container where as ENTRYPOINT instruction cannot be overridden while creating a Container.

11. When we have both CMD and ENTRYPOINT instructions in a Dockerfile?
Answer: CMD instruction will not be executed and CMD instruction will be passed as an argument for ENTRYPOINT.
```


https://habr.com/ru/post/569394/ Docker для Data Scientist'a


https://masteringbackend.com/posts/docker-tutorial

https://habr.com/ru/company/first/blog/658951/ Docker management tools

https://github.com/jesseduffield/lazydocker

https://habr.com/ru/company/southbridge/blog/534334/.  Data /volumes inside Docker

https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose

### Docker for Python

https://testdriven.io/blog/docker-best-practices/

https://pythonspeed.com/articles/base-image-python-docker-images/

https://www.youtube.com/watch?v=BZiwpsnLLYQ Python in Docker

https://www.codingholygrail.com/build-docker-image-for-python-projects

https://habr.com/ru/company/wunderfund/blog/586778/


<https://www.pybootcamp.com/blog/how-to-containerize-python-application/>

https://pure-hack.com/posts/floki/
```
docker run -it  -v /Users/miclub01/GIT/FORK/pelion-ml-demo:/mnt/host mbedos/mbed-os-env /bin/bash
```

<https://habr.com/ru/company/otus/blog/515514/>. ML +Docker


<https://stackoverflow.com/questions/27273412/cannot-install-packages-inside-docker-ubuntu-image>

<https://multipass.run/>

https://monkeysatkeyboards.com/blog/makefiles-age-docker

<https://github.com/wagoodman/dive> see docker layers

### Env
Dockerfile
```
FROM busybox
ENV SHARED_FOLDER
CMD echo $SHARED_FOLDER
```

$ docker build -t my_app .
$ docker run -e SHARED_FOLDER=/xxx 


 
 set environment variables for your containers at runtime via the
 ```
 docker run --env
 ```
 and
 ```
 docker run --env-file commands. 
```
```
--build-arg		Set build-time variables
```
Set build-time variables (--build-arg)
You can use ENV instructions in a Dockerfile to define variable values. These values persist in the built image. However, often persistence is not what you want. Users want to specify variables differently depending on which host they build an image on.

A good example is http_proxy or source versions for pulling intermediate files. The ARG instruction lets Dockerfile authors define values that users can set at build-time using the --build-arg flag:
```
$ docker build --build-arg HTTP_PROXY=http://10.20.30.2:1234 --build-arg FTP_PROXY=http://40.50.60.5:4567 .
```
This flag allows you to pass the build-time variables that are accessed like regular environment variables in the RUN instruction of the Dockerfile. Also, these values don’t persist in the intermediate or final images like ENV values do. You must add --build-arg for each build argument.

Using this flag will not alter the output you see when the ARG lines from the Dockerfile are echoed during the build process.

For detailed information on using ARG and ENV instructions, see the Dockerfile reference.

You may also use the --build-arg flag without a value, in which case the value from the local environment will be propagated into the Docker container being built:
```
$ export HTTP_PROXY=http://10.20.30.2:1234
$ docker build --build-arg HTTP_PROXY .
This is similar to how docker run -e works. Refer to the docker run documentation for more information.
```


## Volumes
```
The -v flag is very flexible. It can bindmount or name a volume with just a slight adjustment in syntax. 
If the first argument begins with a / or ~/, you’re creating a bindmount. Remove that, and you’re naming the volume.

-v /path:/path/in/container mounts the host directory, /path at the /path/in/container
-v path:/path/in/container creates a volume named path with no relationship to the host.

Example
docker run --name=nginx -d -v ~/nginxlogs:/var/log/nginx -p 5000:80 nginx
```
<https://medium.com/bb-tutorials-and-thoughts/understanding-docker-volumes-with-an-example-d898cb5e40d7>

Sharing data between containers:
<https://www.digitalocean.com/community/tutorials/how-to-share-data-between-docker-containers>

```
 find . -type f -not -path '*/\.*' | xargs grep "docker run"

./PelionML_Model/optimize/Makefile:	docker run --rm -t pelion-model-optimize
./PelionML_Model/deploy/Makefile:	docker run --rm -t pelion-model-deploy


./PelionML_Model/README.md:docker run -v "/var/run/docker.sock:/var/run/docker.sock:rw" pelion-model-deploy /workspace/deploy-model.sh

./run.sh:docker run -v "/var/run/docker.sock:/var/run/docker.sock:rw" -v "/Users/miclub01/tmp:/mnt/tmp" pelion-model-deploy /workspace/deploy-model.sh
```
## No space left on device
<https://stackoverflow.com/questions/30604846/docker-error-no-space-left-on-device>
 
 ```
  docker volume rm $(docker volume ls -qf dangling=true)
  
  docker system prune
 ```

<https://medium.com/better-programming/the-ultimate-docker-command-list-d98ef300fe6d> 

<https://stackoverflow.com/questions/39468841/is-it-possible-to-start-a-stopped-container-from-another-container>

It comes down to installing the Docker CLI (or any other tool that can talk to the Docker APIs) in our container and adding a very simple option to our docker invocation:
```
-v /var/run/docker.sock:/var/run/docker.sock
```
or declare a volume likewise for the parent’s service if you are orchestrating a composition of containers with Docker Compose:
volumes:      
 ``` 
   - /var/run/docker.sock:/var/run/docker.sock
 ```
The Docker socket inside the container is shadowed by the socket on the host, thus wiring up the encapsulated environment of the container with the outer world.
It is possible to grant a container access to docker so that it can spawn other containers on your host. You do this by exposing the docker socket inside the container, e.g:
```
docker run -v /var/run/docker.sock:/var/run/docker.sock --name containerB myimage ...
```

<https://docker-py.readthedocs.io/en/stable/>

Dockerfile
```
FROM python:3.8-slim-buster
RUN pip install docker
COPY my.py my.py
CMD python  my.py
```
my.py
```
import sys
import docker
print ("Hello from my.py")
try:
    print("STEP 1")
    client = docker.from_env()
    print("STEP2")
    args={"all" : True}
    all_containers = client.containers.list(args)
    print("STEP3")
    for c in all_containers:
       print(c)
    print("end of list")
except Exception as e:
   print("ERROR")
   print(str(e))
```   

```
docker build -t helloapp:v1 .
docker run -v "/var/run/docker.sock:/var/run/docker.sock:rw" helloapp:v1
docker run helloapp:v1
```

```
Hello from my.py
STEP 1
STEP2
STEP3
<Container: 7386702288>
<Container: 40adbdb08f>
end of list
END
```
Docker run example:
```

docker run -v "/var/run/docker.sock:/var/run/docker.sock:rw" pelion-model-deploy /workspace/deploy-model.sh

docker run   python:3.8-slim-buster  python3 -V;  pwd; bash --version
Python 3.8.2
/Users/michael/D
GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin18)
Copyright (C) 2007 Free Software Foundation, Inc.
```
## Docker

<https://pythonspeed.com/docker/>

<https://habr.com/ru/company/ruvds/blog/488668/> 

<https://youtu.be/zJ6WbK9zFpI> . Docker for Beginners: Full Course

<https://www.manning.com/books/docker-in-action-second-edition> Book

<https://www.udemy.com/home/my-courses/search/?q=docker> my Udemy Docker courses

<https://habr.com/ru/post/486200/> clean Docker images from local machine

<https://habr.com/ru/company/ruvds/blog/486682/> . make for Docker

## Docker Pyhon Image for Datascience

<https://faizanbashir.me/building-python-data-science-container-using-docker-c8e346295669>


### Volumes mount bind
Тома Docker (Docker Volumes) представляют - механизм постоянного хранения данных, потребляемых или производимых приложениями.
<https://docs.docker.com/storage/volumes/> volumes

<https://docs.docker.com/storage/bind-mounts/>

<https://habr.com/ru/company/ruvds/blog/441574/>

Mounting several volumes:
```
docker run -t -i \
  -v '/on/my/host/test1:/on/the/container/test1' \
  -v '/on/my/host/test2:/on/the/container/test2' \
  ubuntu /bin/bash
```

```
docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app \
  --mount type=bind,source="$(pwd)"/target,target=/app2,readonly,bind-propagation=rslave \
  nginx:latest
```  

```
 docker volume create —-name myVolume
 docker volume ls
         DRIVER              VOLUME NAME
         local               myVolume

docker volume inspect myVolume

[
    {
        "CreatedAt": "2019-12-22T04:03:11Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/myVolume/_data",
        "Name": "myVolume",
        "Options": {},
        "Scope": "local"
    }
]

docker volume rm myVolume  # remove volume
docker volume prune .  remove all volumes
```
<https://habr.com/ru/company/ruvds/blog/439980/>

Инструкция WORKDIR позволяет изменить рабочую директорию контейнера. С этой директорией работают инструкции COPY, ADD, RUN, CMD и ENTRYPOINT, идущие за WORKDIR. Вот некоторые особенности, касающиеся этой инструкции:

* Лучше устанавливать с помощью WORKDIR абсолютные пути к папкам, а не перемещаться по файловой системе с помощью команд cd в Dockerfile.
* Инструкция WORKDIR автоматически создаёт директорию в том случае, если она не существует.
* Можно использовать несколько инструкций WORKDIR. Если таким инструкциям предоставляются относительные пути, то каждая из них меняет текущую рабочую директорию.
```
FROM python:3.7.2-alpine3.8
LABEL maintainer="jeffmshale@gmail.com"
# Устанавливаем зависимости
RUN apk add --update git
# Задаём текущую рабочую директорию
WORKDIR /usr/src/my_app_directory
# Копируем код из локального контекста в рабочую директорию образа
COPY . .
# Задаём значение по умолчанию для переменной
ARG my_var=my_default_value
# Настраиваем команду, которая должна быть запущена в контейнере во время его выполнения
ENTRYPOINT ["python", "./app/my_script.py", "my_var"]
# Открываем порты
EXPOSE 8000
# Создаём том для хранения данных
VOLUME /my_volume
```

<https://github.com/eon01/DockerCheatSheet>

<https://habr.com/ru/company/ruvds/blog/441574/> 6 articles

<https://code.visualstudio.com/blogs/2019/10/31/inspecting-containers> Inspecting Containers with VS Code

<https://towardsdatascience.com/how-to-build-slim-docker-images-fast-ecc246d7f4a7>

<https://cameronlonsdale.com/2018/11/26/whats-in-a-docker-image/>

<https://blog.docker.com/2019/07/intro-guide-to-dockerfile-best-practices/>

<https://fire.ci/blog/api-end-to-end-testing-with-docker/> . API end to end testing with Docker

<https://habr.com/ru/company/ruvds/blog/440660/>

<https://habr.com/ru/post/457870/>

<https://awesome-docker.netlify.com/>

<https://offby2.com/posts/001-docker-lesser-known-tips/>

<https://medium.com/learning-cloud-native-go/lets-get-it-started-dc4634ef03b> Go + Docker
<https://habr.com/ru/company/hh/blog/450954/> Java + Docker

<https://github.com/floydhub/dl-docker> Docker image with ML

<https://www.infoq.com/presentations/ing-docker-hadoop> . Docker Data Science Pipeline

<https://blog.softwaremill.com/editing-files-in-a-docker-container-f36d76b9613c> Editing inside docker container

## Nodejs 
<https://jdlm.info/articles/2019/09/06/lessons-building-node-app-docker.html>

<https://habr.com/ru/post/466493/>
```
docker pull node
docker run -it -d --rm -v "$PWD":/app -w=/app -p 80:3000 node node index.js 
```
Но на одном CLI далеко не уедешь. Давайте создадим Dockerfile для нашего сервера.
собрать из этого Dockerfile образ, который мы будем деплоить:

Dockerfile 
```
FROM node
 
WORKDIR /app
RUN cp . /app
 
CMD ["node", "index.js"]
```
собрать из этого Dockerfile образ, который мы будем деплоить:
 ```
 docker build -t username/helloworld-with-docker:0.1.0.
```
контейнер готов. Мы можем запускать его при помощи команды docker run. Таким образом, мы решаем vendor lock-in проблему. Запуск приложения уже не зависит от окружения. Код доставляется вместе с Docker образом. Эти два критерия позволяют нам деплоить приложение в любое место, где мы можем запустить Docker.

сам процесс деплоя уже становится делом техники и вашего окружения разработки. Мы рассмотрим 2 варианта деплоя Docker:

ручной деплой Docker образа;
деплой при помощи Travis-CI.
... 

## Flask and Docker

<https://www.agiratech.com/debugging-python-flask-app-in-docker-container/> 

<https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#.XbLvKyeAs7s.reddit>

<https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04>

<https://testdriven.io/courses/microservices-with-docker-flask-and-react/>

<https://github.com/nickjj/build-a-saas-app-with-flask>

<https://habr.com/ru/company/ruvds/blog/441574/>
Существуют два способа, позволяющих сделать срок жизни данных большим срока жизни контейнера. 

Один из способов заключается в использовании технологии bind mount. При таком подходе к контейнеру можно примонтировать, например, реально существующую папку. Работать с данными, хранящимися в такой папке, смогут и процессы, находящиеся за пределами Docker.


Минусы использования технологии bind mount заключаются в том, что её использование усложняет резервное копирование данных, миграцию данных, совместное использование данных несколькими контейнерами. Гораздо лучше для постоянного хранения данных использовать тома Docker.

<https://habr.com/ru/company/ruvds/blog/439980/>

FROM — задаёт базовый (родительский) образ.

LABEL — описывает метаданные. Например — сведения о том, кто создал и поддерживает образ.

ENV — устанавливает постоянные переменные среды.

RUN — выполняет команду и создаёт слой образа. Используется для установки в контейнер пакетов.

COPY — копирует в контейнер файлы и папки.

ADD — копирует файлы и папки в контейнер, может распаковывать локальные .tar-файлы.

CMD — описывает команду с аргументами, которую нужно выполнить когда контейнер будет запущен. Аргументы могут быть переопределены при запуске контейнера. В файле может присутствовать лишь одна инструкция CMD.

WORKDIR — задаёт рабочую директорию для следующей инструкции.

ARG — задаёт переменные для передачи Docker во время сборки образа.

ENTRYPOINT — предоставляет команду с аргументами для вызова во время выполнения контейнера. Аргументы не переопределяются.

EXPOSE — указывает на необходимость открыть порт.

VOLUME — создаёт точку монтирования для работы с постоянным хранилищем.

<https://www.manifold.co/blog/arguments-and-variables-in-docker-94746642f64b>

<https://towardsdatascience.com/a-short-guide-to-using-docker-for-your-data-science-environment-912617b3603e>

<https://oneraynyday.github.io/dev/2017/08/03/Docker/>

<https://github.com/wagoodman/dive> . explore image

<https://www.youtube.com/watch?v=8hLS1lGk8Fc> make development env using Docker

<https://youtu.be/0mil0KBK4Tw> . russian


Example from <https://github.com/bobbywlindsey/docker-data-science/blob/master/Dockerfile>
<https://towardsdatascience.com/docker-for-data-scientists-5732501f0ba4>

```
# reference: https://hub.docker.com/_/ubuntu/
FROM ubuntu:16.04

# Adds metadata to the image as a key value pair example LABEL version="1.0"
LABEL maintainer="Bobby Lindsey <me@bobbywlindsey.com>"

# Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PATH=/opt/conda/bin:$PATH

# create empty directory to attach volume
RUN mkdir ~/GitProjects && \
    # install Ubuntu packages
    apt-get update && \
    apt-get install -y \
    wget \
    ca-certificates \
    git-core \
    pkg-config \
    tree \
    freetds-dev && \
    # clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    # Install Jupyter config
    mkdir ~/.ssh && touch ~/.ssh/known_hosts && \
    ssh-keygen -F github.com || ssh-keyscan github.com >> ~/.ssh/known_hosts && \
    git clone https://github.com/bobbywlindsey/dotfiles.git && \
    mkdir ~/.jupyter && \
    mkdir -p ~/.jupyter/custom && \
    cp /dotfiles/jupyter_configs/jupyter_notebook_config.py ~/.jupyter/ && \
    cp /dotfiles/jupyter_configs/custom/custom.js ~/.jupyter/custom/ && \
    rm -rf /dotfiles && \
    # Install Anaconda
    echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    # Update Anaconda
    conda update conda && \
    conda update anaconda && \
    conda update --all && \
    # Install Jupyter theme
    pip install msgpack jupyterthemes && \
    jt -t grade3 && \
    # Install other Python packages
    conda install pymssql mkl=2018 && \
    pip install SQLAlchemy \
        missingno \
        json_tricks \
        bcolz \
        gensim \
        elasticsearch \
        psycopg2-binary \
        jupyter_contrib_nbextensions \
        jupyter_nbextensions_configurator \
        pymc3 && \
    jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user && \
    jupyter nbextension enable codefolding/main && \
    jupyter nbextension enable collapsible_headings/main && \
    # remove everything you don't need
    apt-get remove -y wget git-core pkg-config


# Configure access to Jupyter
WORKDIR /root/GitProjects
EXPOSE 8888
CMD jupyter lab --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='data-science'
```

<https://medium.freecodecamp.org/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882>

<https://habr.com/company/microsoft/blog/420159/>

<https://itnext.io/tagged/docker>

<https://hub.docker.com/>

<https://aws.amazon.com/ecr/>

<https://habr.com/company/microsoft/blog/420159/>

<https://itnext.io/3-simple-tricks-for-smaller-docker-images-f0d2bda17d1e>

<http://testdriven.io/> $40 Microservices with Docker Flask React

<https://www.youtube.com/watch?v=8bytAYy22LM&feature=youtu.be>

Download image explicitly: docker pull imageName
or implicitly when starting container.
Containers are the instances of images 

    docker ps -l 
    docker ps -a
    docker images
    docker run -it
    docker run -it busybox sh .   # -it means interactive
    docker run --help
    docker rm $(docker ps -a -q -f status=exited)
    docker rmi   #remove 
    docker images   # local images
    docker pull ubuntu:12.04 # download from docker hub specific version
    docker search # find image
    docker stop    
    
Base images without parent
Child image : apply add-in to parent
    

## Create Dockerfile and make the image

Команда docker build    принимает опциональный тег с флагом -t и путь до директории, в которой лежит Dockerfile.
Username in "docker build" должен соответствовать тому, что использовался при регистрации на Docker hub. 

    docker build -t mlubinsky/myimagenamehere .
    docker push mlubinsky/catnip
    
## Docker Compose
Это инструмент для простого определения и запуска многоконтейнерных Докер-приложений. 
В нем есть файл docker-compose.yml, и с его помощью можно одной командой поднять приложение с набором сервисов.
 
<https://habr.com/ru/post/459618/>

<https://thoughts.theden.sh/post/docker-dev-env/>

<https://habr.com/ru/post/454552/> 

<https://habr.com/post/310460/>

<https://www.toptal.com/devops/getting-started-with-docker-simplifying-devops>

<https://thoughts.theden.sh/post/docker-dev-env/>

<https://oneraynyday.github.io/dev/2017/08/03/Docker/>

<https://docs.docker.com/docker-for-mac/>

<https://engineering.riotgames.com/news/revisiting-docker-and-jenkins>   Docker + Jenkins

## Windows

<https://learnk8s.io/blog/installing-docker-and-kubernetes-on-windows>


## Kubernetes
<https://github.com/kubernetes/minikube>

<https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/>

<https://www.youtube.com/watch?v=zeS6OyDoy78>

<https://habr.com/company/flant/blog/420813/>

[KUB]$ kubectl get nodes \
NAME       STATUS    ROLES     AGE       VERSION \
minikube   Ready     master    1d        v1.10.0  
 
[KUB]$ kubectl cluster-info \
Kubernetes master is running at https://192.168.99.100:8443  \
KubeDNS is running at https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy \

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

[KUB]$ kubectl get cs \
NAME                 STATUS    MESSAGE              ERROR \
controller-manager   Healthy   ok \
scheduler            Healthy   ok \
etcd-0               Healthy   {"health": "true"} 

[KUB]$ kubectl get pods \
NAME                                READY     STATUS    RESTARTS   AGE \
first-deployment-59f6bb4956-hpgcs   1/1       Running   0          1d 

[KUB]$ kubectl get svc \
NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE \
first-deployment   NodePort    10.99.220.26   <none>        80:30158/TCP   1d \
kubernetes         ClusterIP   10.96.0.1      <none>        443/TCP        1d 
