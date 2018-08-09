# Docker
<https://hub.docker.com/>

<https://aws.amazon.com/ecr/>

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
    docker pull ubuntu:12.04 # download from docher hub specific version
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
 
<https://thoughts.theden.sh/post/docker-dev-env/>

<https://habr.com/post/310460/>

<https://www.toptal.com/devops/getting-started-with-docker-simplifying-devops>

<https://thoughts.theden.sh/post/docker-dev-env/>

<https://oneraynyday.github.io/dev/2017/08/03/Docker/>

<https://docs.docker.com/docker-for-mac/>

<https://engineering.riotgames.com/news/revisiting-docker-and-jenkins>   Docker + Jenkins

## Windows

<https://learnk8s.io/blog/installing-docker-and-kubernetes-on-windows>
