https://kubernetes.io/docs/home/

https://habr.com/ru/companies/selectel/articles/956266/

https://habr.com/ru/articles/909260/

https://www.youtube.com/watch?v=hNLQ3tCP8jQ  Kubernetes - Курс по Kubernetes для Начинающих (Bogdan Stashchuk)

https://habr.com/ru/companies/T1Holding/articles/909372/

https://www.youtube.com/watch?v=9ZxZ9gb9pQs

https://www.youtube.com/watch?v=q_nj340pkQo Основы Kubernetes (5 years old!!!)

https://www.youtube.com/watch?v=q_nj340pkQo&list=PLg5SS_4L6LYvN1RqaVesof8KAf-02fJSi

https://selectel.ru/blog/what-is-kubelet/

https://selectel.ru/blog/courses/dive-into-kubernetes/
```
1. A Node is a worker machine provisioned to run Kubernetes. Each Node is managed by the Kubernetes master.

2. A Pod is a logical, tightly-coupled group of application containers that run on a Node.
Containers in a Pod are deployed together and share resources (like data volumes and network addresses). Multiple Pods can run on a single Node.

3. A Service is a logical set of Pods that perform a similar function.
It enables load balancing and service discovery.
It's an abstraction layer over the Pods; Pods are meant to be ephemeral while services are much more persistent.

4. Deployments are used to describe the desired state of Kubernetes.
They dictate how Pods are created, deployed, and replicated.

5. Labels are key/value pairs that are attached to resources (like Pods)
which are used to organize related resources. You can think of them like CSS selectors.
For example:
Environment - dev, test, prod
App version - beta, 1.2.1
Type - client, server, db

6. Ingress is a set of routing rules used to control the external access to Services based on the request host or path.

7. Volumes are used to persist data beyond the life of a container.
They are especially important for stateful applications like Redis and Postgres.
A PersistentVolume defines a storage volume independent of the normal Pod-lifecycle.
It's managed outside of the particular Pod that it resides in.
A PersistentVolumeClaim is a request to use the PersistentVolume by a user.


Oсновные понятия Kubernetes.
***************************
Cluster (кластер) — один или несколько узлов (Node), работающих вместе для запуска контейнеризованных приложений.
Он включает в себя управляющие и рабочие ноды, объединенные общей системой управления.
Кластер обеспечивает масштабируемость, отказоустойчивость и автоматизацию развертывания приложений. 

Node (узел) — физическая или виртуальная машина, которая становится частью вашего кластера.
 Узлы бывают рабочими (на них запускаются приложения) и управляющими (они следят за работой всего кластера).

Master Node (управляющий узел) — это нода, на которой запускаются системные компоненты Kubernetes,
обеспечивающие управление кластером, например, распределение нагрузки, отслеживание состояния подов и обеспечение работы всей инфраструктуры.
 К таким компонентам относятся API-сервер, контроллер-менеджеры и планировщик.
Плоскость управления (Master nodes) управляет рабочими узлами и подами в кластере.
Там располагаются компоненты, которые управляют узлами кластера и предоставляют доступ к API.

 
Worker Node (рабочий узел) — нода, на которой непосредственно запускаются поды с контейнерами.
Этот узел обеспечивает работу приложений, управление их ресурсами и взаимодействие с управляющими нодами.
Worker nodes состоит из компонентов:
-- kubelet - сервис или агент, который контролирует запуск компонентов (контейнеров) кластера
-- kube-proxy - конфигурирует правила сети на узлах



Control plane состоит из компонентов:
```
### Pods
```
Pod (под) — один или несколько контейнеров, которые собраны в одну сущность
и могут быть запущены как одно приложение.'
 Поды — это минимальная единица развертывания в Kubernetes.
 это абстрактный объект в кластере K8S,
который состоит из одного или нескольких контейнеров
с общим хранилищем и сетевыми ресурсами, а также спецификации для запуска контейнеров.

Это главный объект в кластере, в нем прописаны, какие контейнеры должны быть запущены,
количество экземпляров или реплик, политика перезапуска, лимиты, подключаемые ресурсы,
узел кластера для размещения.


Container (контейнер) — изолированный экземпляр приложения или его части, работающий внутри пода.
Контейнеры содержат все необходимое для работы приложения: код, зависимости, библиотеки и настройки среды.

API-сервер — центральный интерфейс для взаимодействия с кластером Kubernetes.
Он принимает запросы от пользователей и инструментов автоматизации, проверяет их корректность и передает инструкции другим компонентам.
 API-сервер также обеспечивает доступ к хранилищу конфигурации, где хранятся все данные о текущем состоянии кластера.

И вот теперь мы подошли к одному из важнейших элементов этой сложной системы — Kubelet.
 Это незаменимый компонент Kubernetes, который можно сравнить с «исполнителем».
 Он трудится на каждом рабочем узле (Node) и выполняет команды управляющего центра K8s,
чтобы приложения в вашем кластере работали так, как задумано.
 Кроме запуска и остановки, Kubelet отслеживает здоровье контейнеров и подов и сообщает об изменениях управляющему компоненту.
```

https://habr.com/ru/post/589415/

https://habr.com/ru/post/651653/

https://habr.com/ru/company/otus/blog/650231/

https://opensource.com/article/22/2/kubernetes-architecture

https://elastisys.com/designing-and-deploying-scalable-applications-on-kubernetes/

<https://testdriven.io/running-flask-on-kubernetes>

<https://habr.com/company/flant/blog/420813/>

<https://habr.com/post/423481/>

https://buttondown.email/nelhage/archive/two-reasons-kubernetes-is-so-complex/

<https://medium.com/@elliot_f/my-notes-for-certified-kubernetes-application-developer-part-1-core-concepts-d1bab7bc2446>

<https://medium.com/containermind/a-beginners-guide-to-kubernetes-7e8ca56420b6>

<https://habr.com/company/otus/blog/422179/>
```
The machines in the Kubernetes cluster are each given a role within the Kubernetes ecosystem.
One server (or a small group in highly available deployments) functions as the master server.
This server acts as a gateway   for the cluster by exposing an API for users and clients,
health checking other servers, deciding how best to split up and assign work (known as “scheduling”),
and orchestrating communication between other components.
The master server acts as the primary point of contact with the cluster
and is responsible for most of the centralized logic Kubernetes provides.
 The other machines in the cluster are designated as nodes.
```
<https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/>
```
[KUB]$ kubectl get nodes \
NAME STATUS ROLES AGE VERSION \
minikube Ready master 1d v1.10.0

[KUB]$ kubectl cluster-info \
Kubernetes master is running at https://192.168.99.100:8443 \
KubeDNS is running at https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy  

To further debug and diagnose cluster problems, use ‘kubectl cluster-info dump’.

[KUB]$ kubectl get cs \
NAME STATUS MESSAGE ERROR \
controller-manager Healthy ok \
scheduler Healthy ok \
etcd-0 Healthy {“health”: “true”}

[KUB]$ kubectl get pods \
NAME READY STATUS RESTARTS AGE \
first-deployment-59f6bb4956-hpgcs 1/1 Running 0 1d

```
<https://www.youtube.com/watch?v=zeS6OyDoy78>

<https://habr.com/company/flant/blog/420813/>


## Pod
<https://mfarache.github.io/mfarache/Understanding-Kubernetes-Pods/>

<https://habr.com/company/flant/blog/415393/>

YAML manifest file
```
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: default
spec:
  containers:
  - image: busybox
    command:
      - sleep
      - "3600"
    name: busybox
```

## Minikube

<https://github.com/kubernetes/minikube>

<https://habr.com/company/flant/blog/333470/>

<https://mfarache.github.io/mfarache/Installing-Kubernetes-using-Minikube/>

<https://github.com/scholzj/aws-minikube>

##  Links
 
<https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes>

<https://www.katacoda.com/courses/kubernetes>

<https://www.confluent.io/blog/getting-started-apache-kafka-kubernetes/>

 

<https://www.infoq.com/presentations/serverless-containers-cloud-apps>

<https://www.infoq.com/presentations/serverless-patterns-antipatterns>


### Install on Mac

You can install Kubernetes on your MacBook in a few different ways — depending on your goals
(e.g., learning kubectl, testing clusters, building manifests, etc.). Here's a breakdown:

✅ Easiest Way: Use Docker Desktop (with Kubernetes)
🧰 What you need:
Docker Desktop (includes a single-node Kubernetes cluster)

🪛 Steps:
Download Docker Desktop
👉 https://www.docker.com/products/docker-desktop

Install Docker Desktop and start the app.

Enable Kubernetes:

Go to Settings → Kubernetes → Check “Enable Kubernetes”

Click “Apply & Restart”

Wait a bit — Docker will install and start a local Kubernetes cluster.

Once it’s ready, test it:

kubectl get nodes

✅ Alternative: Use Minikube (also very popular)  
📦 What is it?
Minikube creates a local Kubernetes cluster using a VM or container runtime.

🪛 Install Steps:
Install Homebrew (if not installed):
 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Minikube:
 
brew install minikube

Start a cluster:
 
minikube start

Check cluster:

kubectl get nodes
Optional: Access Kubernetes dashboard:

 
minikube dashboard  
✅ Bonus: Install kubectl (if not already)
 
brew install kubectl
🧪 Other options for advanced users:  
Kind (Kubernetes IN Docker) — lightweight clusters for testing

k3s — minimal Kubernetes distribution

Rancher Desktop — GUI alternative to Docker Desktop with Kubernetes

🤔 Which one should you choose?
```
Tool	                                 Good for	GUI?	             Notes
Docker Desktop  - 	Easiest setup            	✅ Yes	    Great for beginners  
Minikube	       - More control & flexibility	❌ CLI	     Lightweight & widely used  
Kind	 - Advanced testing/dev workflows	      ❌ CLI	     Good for CI/CD-style dev use  
Rancher - Desktop	GUI alternative to Docker 	✅ Yes	    Uses k3s internally
```



#### Russian Links 

🔗 https://kubernetes.io/ru/docs/


📺 Channels You Might Find Useful
Some Russian-speaking YouTube channels often cover DevOps and Kubernetes topics:

Уголок Задрота — DevOps and cloud-related tutorials in Russian.

Otus Online Education — Offers courses and webinars, often with Kubernetes content.

Флант / flant.ru — A Russian DevOps company that shares Kubernetes content.

Academy DevOps — Focuses on Kubernetes, Docker, and CI/CD in Russian.

🛠️ Tips
Use YouTube’s Filters > Language (if available) to try narrowing results by language.

Set your YouTube interface language to Russian in account settings for more relevant recommendations.

Use Subtitles/CC filter if you’re open to watching English videos with Russian subtitles.

Would you like me to pull up a few recent videos in Russian about Kubernetes?

Slach/k8s-russian.video: Kubernetes по русски
github.com
​Here are some recent Russian-language YouTube resources to help you learn Kubernetes:​

📺 YouTube Playlists
Kubernetes на Русском Языке
A beginner-friendly series explaining Kubernetes concepts in simple terms, including local cluster setup on Windows and AWS deployment.

Кубернетес на русском: практика + теория
A comprehensive free course covering both theoretical and practical aspects of Kubernetes.

🎥 Individual Videos
Основы Kubernetes: что такое кластер (2024)

Что такое Kubernetes? Для чего используют k8s
A brief history and real-world applications of Kubernetes.​
YouTube

Как запустить проект в Kubernetes за 60 минут
A practical guide to deploying a project in Kubernetes within an hour.​
YouTube

🧰 Additional Resource
Slach/k8s-russian.video GitHub Repository
A curated collection of Russian-language Kubernetes video tutorials and resources.​


🔗 https://kubernetes.io/ru/docs/

This is the Russian localization of the official Kubernetes website. It includes translated versions of key documents such as:

Основы Kubernetes (Kubernetes Basics)

Руководства по установке и конфигурации (Setup & Configuration Guides)

Справочник по kubectl

Архитектура и концепции Kubernetes

...and more.

Keep in mind that not all content is always fully up to date in the Russian version, so for the most recent details, you might occasionally need to refer to the English version at https://kubernetes.io/docs/.

Need help navigating it or want a quick translation of a specific section?

🔍 Search Phrases to Use
Try these Russian search phrases directly in the YouTube search bar:

Kubernetes на русском (Kubernetes in Russian)

Обучение Kubernetes (Kubernetes training)

Kubernetes для начинающих (Kubernetes for beginners)

Kubernetes уроки (Kubernetes tutorials)

Kubernetes курс (Kubernetes course)

Kubernetes кластер настройка (Kubernetes cluster setup)

📺 Channels You Might Find Useful
Some Russian-speaking YouTube channels often cover DevOps and Kubernetes topics:

Уголок Задрота — DevOps and cloud-related tutorials in Russian.

Otus Online Education — Offers courses and webinars, often with Kubernetes content.

Флант / flant.ru — A Russian DevOps company that shares Kubernetes content.

Academy DevOps — Focuses on Kubernetes, Docker, and CI/CD in Russian.

🛠️ Tips
Use YouTube’s Filters > Language (if available) to try narrowing results by language.

Set your YouTube interface language to Russian in account settings for more relevant recommendations.

Use Subtitles/CC filter if you’re open to watching English videos with Russian subtitles.

Would you like me to pull up a few recent videos in Russian about Kubernetes?

You said:
Please pull up a few recent videos in Russian about Kubernetes
ChatGPT said:
Favicon
Slach/k8s-russian.video: Kubernetes по русски
github.com
​Here are some recent Russian-language YouTube resources to help you learn Kubernetes:​

📺 YouTube Playlists
Kubernetes на Русском Языке
A beginner-friendly series explaining Kubernetes concepts in simple terms, including local cluster setup on Windows and AWS deployment.

Кубернетес на русском: практика + теория
A comprehensive free course covering both theoretical and practical aspects of Kubernetes.

🎥 Individual Videos
Основы Kubernetes: что такое кластер (2024)
An introductory video explaining the concept of Kubernetes clusters.​
 

Что такое Kubernetes? Для чего используют k8s
A brief history and real-world applications of Kubernetes.​
YouTube

Как запустить проект в Kubernetes за 60 минут  
A practical guide to deploying a project in Kubernetes within an hour.​
YouTube

🧰 Additional Resource
Slach/k8s-russian.video GitHub Repository
A curated collection of Russian-language Kubernetes video tutorials and resources.​

 
Links
 ```
Slach/k8s-russian.video: Kubernetes по русски
github.com
Citations
FaviconYouTube
Kubernetes на Русском Языке - YouTube
1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке · 2-K8s - Поднятие простого Локального K8s Cluster на Windows · 3-K8s - Поднятие Кластера в AWS ...
FaviconYouTube
Кубернетес (kubernetes) на русском: практика + то что ... - YouTube
Курс лекций по kubernetes на русском языке. Курс полностью бесплатный и выложен полностью на youtube. В курсе мы разбираем практическое применение k8s ...
FaviconYouTube
1. Основы Kubernetes: что такое кластер (2024) - YouTube
May 29, 2024 — 2. Основы Kubernetes: для чего создан Kubernetes (2024). javabegin · 863 views ; 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
FaviconYouTube
Что такое Kubernetes? Для чего используют k8s - YouTube
February 11, 2022 — в этом ролике краткая предыстория о том, как появился Kubernetes и пример из жизни, где применяется k8s. А в конце -- объяснение, ...
FaviconYouTube
Как запустить проект в Kubernetes за 60 минут - YouTube
April 29, 2021 — Kubernetes - https://vk.cc/c28HLk Kubernetes — сложная для внедрения технология ... 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
More
FaviconYouTube
1. Основы Kubernetes: что такое кластер (2024) - YouTube
May 29, 2024 — 2. Основы Kubernetes: для чего создан Kubernetes (2024). javabegin · 863 views ; 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
FaviconYouTube
6. Основы Kubernetes: понятия Pod и Node (2024) - YouTube
May 29, 2024 — Comments1 ; 7. Основы Kubernetes: установка minikube (2024). javabegin · 896 views ; Kubernetes для разработчиков | Илья Бочаров. Yappi Days · 10K ...
FaviconYouTube
Курс по Kubernetes для Начинающих - YouTube
December 27, 2023 — Полный курс Kubernetes [6 ЧАСОВ] https://sale.stashchuk.com/k8s Полный курс Docker [7 ЧАСОВ] https://sale.stashchuk.com/docker Полный ...
FaviconYouTube
Что такое Kubernetes? Для чего используют k8s - YouTube
February 11, 2022 — в этом ролике краткая предыстория о том, как появился Kubernetes и пример из жизни, где применяется k8s. А в конце -- объяснение, ...
FaviconYouTube
Урок 1: Введение в Kubernetes. Вечерняя школа - YouTube
September 30, 2021 — Курс одинаково полезен независимо от платформы, где работает ваш Kubernetes. Kubernetes База — https://to.slurm.io/-SXDlQ Kubernetes Мега ...
FaviconYouTube
Как запустить проект в Kubernetes за 60 минут - YouTube
April 29, 2021 — Kubernetes - https://vk.cc/c28HLk Kubernetes — сложная для внедрения технология ... 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
FaviconYouTube
1-kuberentes. Введение. Кубернетес на русском ( Практический ...
October 5, 2020 — Comments3 · 2-kuberentes. · Complete Kubernetes Course - From BEGINNER to PRO · Наш опыт с Kubernetes в небольших проектах / Дмитрий Столяров ( ...
FaviconYouTube
1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке
January 17, 2020 — devops #девопс #kubernetes #ityoutubersru 1-K8s - Основы Kubernetes Если помог, поддержите парой баксов, хотябы Канадских ...
FaviconYouTube
Kubernetes на Русском Языке - YouTube
1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке · 2-K8s - Поднятие простого Локального K8s Cluster на Windows · 3-K8s - Поднятие Кластера в AWS ...
FaviconYouTube
Кубернетес (kubernetes) на русском: практика + то что ... - YouTube
Курс лекций по kubernetes на русском языке. Курс полностью бесплатный и выложен полностью на youtube. В курсе мы разбираем практическое применение k8s ...
 
Slach/k8s-russian.video: Kubernetes по русски
github.com
Citations
 
Kubernetes на Русском Языке - YouTube
1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке · 2-K8s - Поднятие простого Локального K8s Cluster на Windows · 3-K8s - Поднятие Кластера в AWS ...
FaviconYouTube
Кубернетес (kubernetes) на русском: практика + то что ... - YouTube
Курс лекций по kubernetes на русском языке. Курс полностью бесплатный и выложен полностью на youtube. В курсе мы разбираем практическое применение k8s ...
FaviconYouTube
1. Основы Kubernetes: что такое кластер (2024) - YouTube
May 29, 2024 — 2. Основы Kubernetes: для чего создан Kubernetes (2024). javabegin · 863 views ; 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
FaviconYouTube
Что такое Kubernetes? Для чего используют k8s - YouTube
February 11, 2022 — в этом ролике краткая предыстория о том, как появился Kubernetes и пример из жизни, где применяется k8s. А в конце -- объяснение, ...
FaviconYouTube
Как запустить проект в Kubernetes за 60 минут - YouTube
April 29, 2021 — Kubernetes - https://vk.cc/c28HLk Kubernetes — сложная для внедрения технология ... 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
More
FaviconYouTube
1. Основы Kubernetes: что такое кластер (2024) - YouTube
May 29, 2024 — 2. Основы Kubernetes: для чего создан Kubernetes (2024). javabegin · 863 views ; 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
FaviconYouTube
6. Основы Kubernetes: понятия Pod и Node (2024) - YouTube
May 29, 2024 — Comments1 ; 7. Основы Kubernetes: установка minikube (2024). javabegin · 896 views ; Kubernetes для разработчиков | Илья Бочаров. Yappi Days · 10K ...
FaviconYouTube
Курс по Kubernetes для Начинающих - YouTube
December 27, 2023 — Полный курс Kubernetes [6 ЧАСОВ] https://sale.stashchuk.com/k8s Полный курс Docker [7 ЧАСОВ] https://sale.stashchuk.com/docker Полный ...
FaviconYouTube
Что такое Kubernetes? Для чего используют k8s - YouTube
February 11, 2022 — в этом ролике краткая предыстория о том, как появился Kubernetes и пример из жизни, где применяется k8s. А в конце -- объяснение, ...
FaviconYouTube
Урок 1: Введение в Kubernetes. Вечерняя школа - YouTube
September 30, 2021 — Курс одинаково полезен независимо от платформы, где работает ваш Kubernetes. Kubernetes База — https://to.slurm.io/-SXDlQ Kubernetes Мега ...
FaviconYouTube
Как запустить проект в Kubernetes за 60 минут - YouTube
April 29, 2021 — Kubernetes - https://vk.cc/c28HLk Kubernetes — сложная для внедрения технология ... 1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке.
FaviconYouTube
1-kuberentes. Введение. Кубернетес на русском ( Практический ...
October 5, 2020 — Comments3 · 2-kuberentes. · Complete Kubernetes Course - From BEGINNER to PRO · Наш опыт с Kubernetes в небольших проектах / Дмитрий Столяров ( ...
FaviconYouTube
1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке
January 17, 2020 — devops #девопс #kubernetes #ityoutubersru 1-K8s - Основы Kubernetes Если помог, поддержите парой баксов, хотябы Канадских ...
FaviconYouTube
Kubernetes на Русском Языке - YouTube
1-K8s - Основы Kubernetes - Кубернетес на ОЧЕНЬ простом языке · 2-K8s - Поднятие простого Локального K8s Cluster на Windows · 3-K8s - Поднятие Кластера в AWS ...
FaviconYouTube
Кубернетес (kubernetes) на русском: практика + то что ... - YouTube
Курс лекций по kubernetes на русском языке. Курс полностью бесплатный и выложен полностью на youtube. В курсе мы разбираем практическое применение k8s ...
```
<http://okigiveup.net/a-tutorial-introduction-to-kubernetes/>

<https://news.ycombinator.com/item?id=17462043>

<https://www.stavros.io/posts/kubernetes-101/>
