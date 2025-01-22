https://kubernetes.io/docs/home/

https://selectel.ru/blog/what-is-kubelet/

https://selectel.ru/blog/courses/dive-into-kubernetes/
```
основные понятия Kubernetes.

Cluster (кластер) — один или несколько узлов (Node), работающих вместе для запуска контейнеризованных приложений.
Он включает в себя управляющие и рабочие ноды, объединенные общей системой управления.
Кластер обеспечивает масштабируемость, отказоустойчивость и автоматизацию развертывания приложений. 

Node (узел) — физическая или виртуальная машина, которая становится частью вашего кластера.
 Узлы бывают рабочими (на них запускаются приложения) и управляющими (они следят за работой всего кластера).

Master Node (управляющий узел) — это нода, на которой запускаются системные компоненты Kubernetes,
обеспечивающие управление кластером, например, распределение нагрузки, отслеживание состояния подов и обеспечение работы всей инфраструктуры.
 К таким компонентам относятся API-сервер, контроллер-менеджеры и планировщик.

Kubernetes: большой обзор технологии, установка и настройка
Worker Node (рабочий узел) — нода, на которой непосредственно запускаются поды с контейнерами.
Этот узел обеспечивает работу приложений, управление их ресурсами и взаимодействие с управляющими нодами.

Pod (под) — один или несколько контейнеров, которые собраны в одну сущность и могут быть запущены как одно приложение.'
 Поды — это минимальная единица развертывания в Kubernetes.

Container (контейнер) — изолированный экземпляр приложения или его части, работающий внутри пода.
Контейнеры содержат все необходимое для работы приложения: код, зависимости, библиотеки и настройки среды.

API-сервер — центральный интерфейс для взаимодействия с кластером Kubernetes.
Он принимает запросы от пользователей и инструментов автоматизации, проверяет их корректность и передает инструкции другим компонентам.
 API-сервер также обеспечивает доступ к хранилищу конфигурации, где хранятся все данные о текущем состоянии кластера.

И вот теперь мы подошли к одному из важнейших элементов этой сложной системы — Kubelet.
 Это незаменимый компонент Kubernetes, который можно сравнить с «исполнителем».
 Он трудится на каждом рабочем узле (Node) и выполняет команды управляющего центра K8s, чтобы приложения в вашем кластере работали так, как задумано.
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

The machines in the Kubernetes cluster are each given a role within the Kubernetes ecosystem. One server (or a small group in highly available deployments) functions as the master server. This server acts as a gateway   for the cluster by exposing an API for users and clients, health checking other servers, deciding how best to split up and assign work (known as “scheduling”), and orchestrating communication between other components. The master server acts as the primary point of contact with the cluster and is responsible for most of the centralized logic Kubernetes provides. The other machines in the cluster are designated as nodes.

<https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/>

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



<http://okigiveup.net/a-tutorial-introduction-to-kubernetes/>

<https://news.ycombinator.com/item?id=17462043>

<https://www.stavros.io/posts/kubernetes-101/>
