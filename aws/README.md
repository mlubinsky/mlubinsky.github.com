
<https://www.slideshare.net/AmazonWebServices/getting-started-on-aws-awsome-day-dallas-2018>

<https://medium.freecodecamp.org/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e>

 <https://habr.com/company/abdoc/blog/352856/>
 
 TerraForm vs CloudFormation
 
 До недавнего времени разработка бессерверных приложений сильно осложнялась тем, что не было средств полноценного локального тестирования lambda-функций и API. 
При создании приложений нужно было или работать все время онлайн, редактируя код в браузере, 
или постоянно архивировать и загружать в облако исходный код lambda-функций. 

Летом 2017 произошел прорыв. AWS создал новый упрощенный стандарт шаблонов CloudFormation, который они назвали Serverless Application Model (SAM) и одновременно 
запустили проект sam-local. Обо всем по порядку.

Amazon CloudFormation — это такой сервис, который позволят описывать всю нужную для вашего приложения инфраструктуру AWS с помощью файла шаблона в формате JSON или YAML. 
Это очень-очень удобная штука. Потому что без нее вам нужно вручную через веб-консоль или командный интерфейс 
создавать множество нужных вам ресурсов: ламбда-функции, база данных, API, роли и политики… 

С помощью CloudFormation инфраструктуру можно нарисовать или в специальном дизайнере, или написать ее руками в шаблоне. 
 В любом случае в итоге получается файл шаблона, 
с помощью которого дальше можно в пару-тройку кликов или одной командой поднять все, что нужно для приложения. 
А дальше при необходимости вносить изменения в этот шаблон и применять их опять же одной командой. 
Это делает поддержку инфраструктуры приложения гораздо легче. Получается, инфраструктура, как код.

CloudFormation прекрасен, его шаблоны позволяют описать практически 100% ресурсов AWS. Но из-за его универсальности это достаточно «многословный» формат — 
шаблоны могут быстро вырастать до приличных размеров. Осознавая это и преследуя цель сделать создание бессерверных приложений проще, AWS создали новый формат SAM. 

Можно условно считать, что обычные шаблоны CloudFormation пишутся на языке низкого уровня. 
А шаблоны SAM — на языке высокого уровня, таким образом, позволяя 
описывать инфраструктуру бессерверных приложений при помощи упрощенного синтаксиса. 
 Шаблоны SAM трансформируются CloudFront в обычные шаблоны при деплое.

Что же такое sam-local? Это инструмент командной строки, позволяющий работать локально с бессерверными приложениями, описанными шаблонами SAM. 
Sam-local позволяет тестировать lambda-функции, генерировать события от различных сервисов AWS, запускать API Gateway, проверять шаблоны SAM — и всё это локально!

Sam-local использует docker-контейнер для эмуляции API Gateway и Lambda. Принцип работы следующий. При запуске sam-local ищет файл шаблона SAM папке проекта. 
 Он анализирует файл шаблона и запускает в docker-контейнере выделенные в шаблоне ресурсы: открывает API и подключает к ним ламбда-функции. 
 Причем поддержка очень близкая к работе реальных lambda-функций 
 (лимиты, показывается объем использованной памяти и длительность выполнения). 
          
 <https://github.com/open-guides/og-aws>
 
 <https://epsagon.com/blog/how-to-handle-aws-lambda-errors-like-a-pro>
 
 <https://news.ycombinator.com/item?id=17064676>
 
 <https://www.serverlessops.io/blog/serverless-ops-aws-lambda-serverless-development-workflow>
 
 <https://medium.com/epsagon/the-right-way-to-distribute-messages-effectively-in-serverless-applications-f427e4229e67>
 
 <https://medium.com/epsagon/aws-lambda-internals-part-2-going-deeper-1e12b9d2515f>
 
 <https://blog.sourcerer.io/full-guide-to-developing-rest-apis-with-aws-api-gateway-and-aws-lambda-d254729d6992>
 
 <https://servers.lol>
 
 <https://serverless.com/>
 
 <https://habr.com/company/funcorp/blog/354394/> AWS
 
 <https://read.acloud.guru/six-months-of-serverless-lessons-learned-f6da86a73526> 
 
 <https://www.jefclaes.be/2017/12/passing-aws-certified-solutions.html>  AWS exam
 
 <https://github.com/JefClaes/amazon-redshift-fundamentals> Redshift
 
 <https://www.rainerhahnekamp.com/en/single-instance-ecs-setup/>
 
 <https://itnext.io/creating-a-blueprint-for-microservices-and-event-sourcing-on-aws-291d4d5a5817>
 
 <https://www.nodexplained.com/blog-detail/2018/04/27/explore-the-amazon-web-services-management-console>
 
 <https://medium.com/epsagon/lambda-internals-exploring-aws-lambda-462f05f74076>   AWS
 
 <https://itnext.io/creating-a-blueprint-for-microservices-and-event-sourcing-on-aws-291d4d5a5817>
 
 <https://blog.sicara.com/deploy-serverless-lambda-s3-api-aws-2cf99b8f34ae>
 
 <https://itnext.io/create-ftp-on-aws-ec2-f6e57d4d7f25>  FTP on AWS
 
 <https://loige.co/aws-command-line-s3-content-from-stdin-or-to-stdout/>
 
 <https://read.acloud.guru/how-we-built-a-big-data-analytics-platform-on-aws-for-100-large-users-for-under-2-a-month-b37425b6cc4>
 
 <https://www.javacodegeeks.com/tag/amazon-aws>
 
 
