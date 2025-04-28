https://sites.google.com/site/mlubinsky/performance

https://sites.google.com/site/mikelubinsky/performance

https://habr.com/ru/companies/jugru/articles/486712/    
https://habr.com/ru/companies/jugru/articles/527186/ Поговорим про перформанс-анализ
CPU-bound бенчмарки и   memory-bound бенчмарки

https://habr.com/ru/articles/43905/
```
Режим минимизации времени выполнения одного запроса (Latency mode).  
Предполагает создание и выполнение одного запроса для вывода модели на выбранном устройстве. Следующий запрос на вывод создается по завершении предыдущего.  
Количество сгенерированных запросов определяется числом итераций цикла тестирования модели.
 
Режим минимизации времени выполнения набора запросов (Throughput mode). 

Bandwidth — это ширина канала. Сколько можно прокачать данных за секунду, сколько можно пустить инструкций чтобы полностью загрузить ALU и так далее.
Latency — это длина канала, то есть через какое время к тебе придут данные, которые ты попросил.
 Через сколько тактов к тебе придет запрошенный бит из памяти, через сколько тактов будет готов результат инструкции, когда команда пройдет до конца пайплайна и так далее.
И они, разумеется, друг на друга влияют. Как только нужен результат, а делать больше нечего — весь bandwidth простаивает из-за latency.
Запросили память, которой нет в кеше — сидим, ждем память. Захотели выполнить инструкцию, которой необходим результат предыдущей — ждем ее выполнения. Это создает «пузыри» в канале и соответственно уменьшает загрузку.

Херб в презентации использует пример нефтепровода, он вполне наглядный.
Можно прокачивать дикое количество баррелей в минуту, но каждый баррель идет до места назначения несколько дней.
В чистом виде bandwidth и latency.

Практически важный момент в том, что bandwidth всегда легко покупать.
Поставить два процессора, брать из памяти за раз в два раза больше данных, поставить два компьютера в конце концов.
 Latency же гораздо дороже — две женщины не родят ребенка за 4.5 месяцев, и продвигается оно только прогрессом — увеличивать частоты, уменьшать размеры элементов, менять технологию и так далее.
```

https://habr.com/ru/articles/497290/ Повышение производительности с использованием uop-кэша на Sandy Bridge+

https://habr.com/ru/articles/107621/ Поиск и решение проблем масштабируемости на примере многоядерных процессоров Intel Core 2 (часть 2)

https://habr.com/ru/companies/intel/articles/171079/ 

https://habr.com/ru/companies/tbank/articles/514314/ Load Testing:  LoadRunner, JMEter, Gatling

https://habr.com/ru/companies/ydb/articles/763938/  TPC-C  измеряющая количество обработанных заказов в минуту. Используется несколько транзакций для имитации бизнес-активности обработки заказа, и каждая транзакция должна укладываться в заданное время ответа. Метрика производительности выражается в транзакциях-в-минуту-C (tpmC)».

https://habr.com/ru/companies/otus/articles/523148/  FlameGraph

https://habr.com/ru/companies/postgrespro/articles/720272/ Postgres 

https://habr.com/ru/articles/151560/ mySQL

https://habr.com/ru/companies/cloudera/articles/560246/ Apache Spark 3 performance

https://habr.com/ru/articles/243045/ NetApp

https://habr.com/ru/companies/intel/articles/165903/ NUMA

### Go performance
https://habr.com/ru/companies/vk/articles/902820/

https://habr.com/ru/articles/596755/ Если объединить структурный поиск по коду через gogrep и фильтрацию результатов через perf-heatmap, то мы получим profile-guided поиск по коду.

https://github.com/quasilyte/perf-heatmap

https://github.com/google/pprof

https://habr.com/ru/companies/kaspersky/articles/591725/


### Performance 
 
https://www.infoq.com/articles/lessons-learned-performance-testing/ О правильном использовании памяти в NUMA-системах под управлением ОС Linux

https://habrahabr.ru/company/mailru/blog/254843/ Проектирование высоконагруженных систем

### Syslog  
https://devconnected.com/syslog-the-complete-system-administrator-guide/
https://news.ycombinator.com/item?id=20612791

### Concurrency 
https://github.com/heathermiller/dist-prog-book/blob/master/chapter/2/futures.md
http://nikgrozev.com/2015/07/14/overview-of-modern-concurrency-and-parallelism-concepts/

https://facebook.github.io/watchman/ . watch the file and directory change

### JMeter 
In docker:
http://dockerlabs.collabnix.com/play-with-docker/jmeter-docker/
https://softwaretester.info/apache-jmeter-and-docker/
https://hub.docker.com/r/justb4/jmeter/

https://habr.com/ru/articles/582632/ JDK Flight Recorder
 
https://www.blazemeter.com/blog/make-use-of-docker-with-jmeter-learn-how/
 


```
docker build -t jmeter .
docker image ls
docker volume create myVolume
docker volume inspect myVolume


```
in Dockerfile:
                                                                                   ```
```                                                                                  
ARG JMETER_VERSION="5.2.1"

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


```


https://stackoverflow.com/questions/35960164/jmeter-and-docker
https://medium.com/@vepo/dockerized-jmeter-84228733e306

https://habr.com/ru/post/339014/

 brew install jmeter 
 JMeter -v
 brew upgrade jmeter
 
  
 
Don't use GUI mode for load testing , only for Test creation and Test debugging.
For load testing, use CLI Mode (was NON GUI):
  ``` jmeter -n -t [jmx file] -l [results file] -e -o [Path to web report folder]```

increase Java Heap to meet your test requirements:
   Modify current env variable HEAP="-Xms1g -Xmx1g -XX:MaxMetaspaceSize=256m" in the jmeter batch file
Check : https://jmeter.apache.org/usermanual/best-practices.html
```
 jmeter -n :run in command line mode
 jmeter -t testPlax.jmx
 jmeter -l log.txt
``` 
 https://habr.com/ru/post/140310/
 
### Design 
https://habrahabr.ru/company/carprice/blog/340946/   distributed tracing
https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/pdf/Performance_Tuning_Guide/Red_Hat_Enterprise_Linux-7-Performance_Tuning_Guide-en-US.pdf
http://natsys-lab.blogspot.com/2016/09/how-to-analyze-performance-of-your.html
https://www.slideshare.net/profyclub_ru/natsys-lab-tempesta-technologies
https://habrahabr.ru/company/oleg-bunin/blog/316898/
https://github.com/mspnp/performance-optimization/blob/master/Assessing-System-Performance-Against-KPI.md
System performance is primarily concerned with the following factors:

How many operations can the system perform in a given period of time (throughput)?
How many operations can be performed simultaneously (concurrency)?
How long does the system take to perform an operation (response time/latency)?
How much spare capacity does the system have to allow for growth (head-room)?
How many exceptions does the system generate while performing operations (error rate)?


A CPU operates in two modes; user mode and privileged mode.
In user mode, the CPU is executing instructions that constitute the business logic of an application.
In privileged mode, the CPU is performing operating system kernel-level functions such as handling network or file I/O, allocating memory, paging, scheduling and managing threads, and context switching between processes.



https://medium.com/netflix-techblog/linux-performance-analysis-in-60-000-milliseconds-accc10403c55  
https://speakerdeck.com/kaushik/tracing-and-profiling-java-and-native-applications-in-production  
https://habrahabr.ru/company/jugru/blog/337928/  
https://habrahabr.ru/post/171475/ How to test performance  
https://habrahabr.ru/company/airbnb/blog/239829/  

http://www.brendangregg.com/usemethod.html  
http://www.brendangregg.com/perf.html   
http://www.brendangregg.com/blog/2016-10-21/linux-efficient-profiler.html  
http://www.brendangregg.com/flamegraphs.html  
https://medium.com/netflix-techblog/java-in-flames-e763b3d32166  
http://psy-lob-saw.blogspot.co.za/2017/02/flamegraphs-intro-fire-for-everyone.html  
 new option in the JVM: -XX:+PreserveFramePointer, a

Linux: perf, eBPF, SystemTap, and ktap   https://perf.wiki.kernel.org/index.php/Tutorial

Solaris, illumos, FreeBSD: DTrace

Mac OS X: DTrace and Instruments

http://queue.acm.org/detail.cfm?id=2513149   NUMA

https://news.ycombinator.com/item?id=16685452  many diagnostic tools
uptime
dmesg | tail     last 10 system messages, if there are any.
vmstat 1
mpstat -P ALL 1
pidstat 1
iostat -xz 1
free -m
sar -n DEV 1
sar -n TCP,ETCP 1
top
http://cb.vu/unixtoolbox.xhtml

CPUs: sockets, cores, hardware threads (virtual CPUs)
Memory: capacity
Network interfaces
Storage devices: I/O, capacity
Controllers: storage, network cards
Interconnects: CPUs, memory, I/O


https://www.tecmint.com/12-top-command-examples-in-linux/


https://peteris.rocks/blog/htop/ . not only about htop

список запущенных процессов и отсортировать их по использованию памяти :

https://habrahabr.ru/post/140010/ atop

ps -eo pmem,pcpu,rss,vsize,args | sort -k 1 -r | less
pstree

### strace lsof 
strace  - system and network calls
https://habr.com/ru/company/first/blog/467093/
https://habr.com/ru/company/southbridge/blog/478626/

The ltrace utility does for library calls what strace does for system calls

lsof - https://habrahabr.ru/company/ruvds/blog/337934/
To list all the files opened by particular PID
 lsof –p PID

ldd stands for list dynamic dependencies to show shared libraries needed by the library.

https://habrahabr.ru/post/305188/  Linux perf
CPU load:
https://habrahabr.ru/company/infopulse/blog/329206/
https://habrahabr.ru/post/309796/

Memory: https://habrahabr.ru/post/312078/
https://habrahabr.ru/company/yandex/blog/250753/

https://yakking.branchable.com/posts/daemons/

###  Disk I/O 
https://medium.com/@ifesdjeen/on-disk-io-part-1-flavours-of-io-8e1ace1de017  
https://medium.com/@ifesdjeen/on-disk-io-part-2-more-flavours-of-io-c945db3edb13   
http://www.scylladb.com/2017/10/05/io-access-methods-scylla/  

https://habr.com/ru/articles/154235/ Как правильно мерять производительность диска

https://habr.com/ru/articles/168711/


### GDB  
http://www.brendangregg.com/blog/2016-08-09/gdb-example-ncurses.html  
http://rr-project.org/  

### Python 

https://yakking.branchable.com/posts/fast-python/

### C++  
https://habrahabr.ru/company/oleg-bunin/blog/340394/   Profiling C++  
https://habrahabr.ru/post/313686/ Logging in C++  
http://www.baical.net/  
gcc  optimization flags -O1	With -O2	With -O3  
http://agner.org/optimize/optimizing_cpp.pdf?10142017 (PDF)  
https://news.ycombinator.com/item?id=15400396  
https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis  
cppcheck  
http://oclint.org/  
https://www.reddit.com/r/cpp/comments/728xfs/orbit_cc_performance_profiler/  
https://github.com/namhyung/uftrace  
https://www.kdab.com/hotspot-v1-1-0-adds-timeline-recording-features/  

http://cs.yale.edu/homes/aspnes/classes/223/notes.html#performanceTuning  
http://agner.org/optimize/optimizing_cpp.pdf?10142017  
https://habrahabr.ru/post/276607/  
https://habrahabr.ru/company/xakep/blog/258961/  
https://habrahabr.ru/company/intel/blog/279669/  
https://habrahabr.ru/company/intel/blog/277407/  

http://apolukhin.github.io/Boost-Cookbook/  

###  Networking 
https://yakking.branchable.com/posts/basic-networking/
https://yakking.branchable.com/tags/network/
https://eli.thegreenplace.net/2017/concurrent-servers-part-1-introduction/

TCP/IP is a two-part system, functioning as the Internet’s fundamental “control system”. 
IP stands for Internet Protocol; its job is to send and route packets to other computers using the IP headers 
(i.e. the IP addresses) on each packet. 
The second part, 
Transmission Control Protocol (TCP), is responsible for breaking the message or file into smaller packets, 
routing packets to the correct application on the destination computer using the TCP headers, 
resending the packets if they get lost on the way, and reassembling the packets in the correct order once they’ve reached the other end.
https://habrahabr.ru/company/odnoklassniki/blog/266005/


### Web 
https://habrahabr.ru/company/oleg-bunin/blog/340114/
https://www.igvita.com/2013/01/15/faster-websites-crash-course-on-web-performance/
https://medium.freecodecamp.org/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c

https://medium.freecodecamp.org/how-the-web-works-part-iii-http-rest-e61bc50fa0a
http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url/

1. You enter a URL into the browser
2. The browser looks up the IP address for the domain name (DNS server) - http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url/
3. The browser sends a HTTP request to the web server
4. The facebook server responds with a permanent redirect
5. The browser follows the redirect
6. The server will receive the GET request, process it, and send back a response.
7. The server sends back a HTML response
8. The browser begins rendering the HTML
9. The browser sends requests for objects embedded in HTML
10. The browser sends further asynchronous (AJAX) requests


Your browser has a rendering engine that’s responsible for displaying the content. 
The rendering engine receives the content of the resources in small chunks. 
Then there’s an HTML parsing algorithm that tells the browser how to parse the resources.

https://medium.com/@christophelimpalair/developers-what-you-should-know-about-web-performance-550cef1040d8
https://medium.com/gitconnected/debounce-in-javascript-improve-your-applications-performance-5b01855e086

https://github.com/codesenberg/bombardier  
https://github.com/tsenart/vegeta  
https://github.com/wg/wrk  
https://github.com/giltene/wrk2  

Time to complete the 5000000 requests - smaller is better.
Reqs/sec — bigger is better.
Latency — smaller is better
Throughput — bigger is better.
Memory usage — smaller is better.


Don’t load stuff you don’t need
Cache everything you can cache
Compress everything you can compress

https://developers.google.com/web/tools/chrome-devtools/console/console-reference#timestamp

‘measuring performance’ can be separated into two things:
1) A single measurable number that can be used to support a discussion about performance. 
It can be used to set priorities, and be tracked over time. 
It is an indicator of overall performance, and does not aim to capture all the nuance of a site’s performance. 
I will call this the “key performance indicator”.


Example: for  KPI, you decide you will measure the time it takes until a user can begin reading the text on your page

2) Something to help  the web developers, understand where time is being spent loading our site, in all different conditions, 
and to guide us when improving performance. It doesn’t need to be recorded or reported in any formal way. 
I will call this the “ad hoc assessment of factors impacting a site’s performance with the aim of improving said performance”.


<h2>Java Performance</h2>
https://habrahabr.ru/post/349914/   JMH
https://medium.com/techlogs/java-process-in-linux-finding-thread-which-takes-most-cpu-c7b281f0282a
https://raygun.com/blog/java-performance-optimization-tips/
https://www.voxxed.com/2017/09/java-performance-puzzlers-douglas-hawkins/
https://www.cubrid.org/blog/the-principles-of-java-application-performance-tuning
http://www.javaperformancetuning.com/
https://habrahabr.ru/company/jugru/blog/338732/
http://javapapers.com/java/java-string-vs-stringbuilder-vs-stringbuffer-concatenation-performance-micro-benchmark/

Do not  String concat with + is highly discouraged - instead use Stringbuilder or StringBuffer.

https://habrahabr.ru/company/jugru/blog/338928/
https://habrahabr.ru/company/jugru/blog/320620/
http://www.idryman.org/blog/2013/09/28/java-fast-io-using-java-nio-api/

https://en.wikipedia.org/wiki/Java_Virtual_Machine_Tools_Interface  - Java Virtual Machine Tool Interface (JVM TI)
продуктовая версия HotSpot JVM предлагает около 600 так называемых расширенных опций (это те опции, которые начинаются с -ХХ),
а debug-сборка включает более 1200 таких опций (чтобы получить полный список, вы можете использовать ключ -XX:+PrintFlagsFinal).

https://habrahabr.ru/company/getintent/blog/302910/


сборщики мусора:
Java Heap space is divided in to two regions Young and Old. 
The Young generation is meant to hold short-lived objects while the Old generation is intended for objects with longer lifetimes.

The Young generation is further divided into three regions [Eden, Survivor1, Survivor2].

A simplified description of the garbage collection procedure: 
When Eden is full, a minor GC is run on Eden and objects that are alive from Eden and Survivor1 are copied to Survivor2. 
The Survivor regions are swapped. If an object is old enough or Survivor2 is full, it is moved to Old. 
Finally when Old is close to full, a full GC is invoked.

1. Serial Garbage Collector  -XX:+UseSerialGC
2. Parallel Garbage Collector
3. CMS Garbage Collector (Concurrent Mark Sweep)  XX:+USeParNewGC
4. G1 Garbage Collector –XX:+UseG1GC   -XX:+UseStringDeduplication

CMS позволяет значительно сокращать задержки, связанные со сборкой мусора. Однако при его использовании приходится неизбежно сталкиваться с двумя основными проблемами, которые и создают необходимость в дополнительной настройке:
- Фрагментация памяти
- Высокий allocation rate

Положительно повлиять на первый параметр можно путем контролирования promotion rate показателя. 
Для этого необходимо определить, какой объем объектов попадает в Tenured, а какой «умирает молодым» в Eden области.

Тестирование производилось со следующими параметрами:
-XX:+UseConcMarkSweepGC
-XX:NewRatio=1, 3, 5

для логирования использовались:
-XX:+PrintGCDetails -XX:+PrintGC -XX:+PrintGCTimeStamps -XX:+PrintTenuringDistribution -XX:+PrintGCDateStamps -XX:+PrintCMSInitiationStatistics -XX:PrintCMSStatistics=1

G1
-XX:+UseG1GC
-XX:MaxGCPauseMillis=100, 60, 40

 JConsole,
 JITwatch
 Flight Recorder
 http://javapapers.com/java/java-garbage-collection-monitoring-and-analysis/

https://habrahabr.ru/post/270059/  
https://habrahabr.ru/company/jugru/blog/280420/  
https://habrahabr.ru/company/getintent/blog/302910/ Garbage collector  
https://www.youtube.com/user/profyclub/  
https://habrahabr.ru/company/wunderfund/blog/325634/ Google Benchmark Library  
https://habrahabr.ru/post/323010/  REST API for high performance  

https://habrahabr.ru/company/jugru/blog/320620/  
https://habrahabr.ru/company/jugru/blog/338928/  
https://habrahabr.ru/company/jugru/blog/338732/  
https://habrahabr.ru/company/netologyru/blog/337842/  
https://habrahabr.ru/post/336104/  
https://habrahabr.ru/post/185010/  
https://habrahabr.ru/company/jugru/blog/335852/  
https://habrahabr.ru/company/oleg-bunin/blog/335260/  
https://habrahabr.ru/company/mailru/blog/109916/s  
https://habrahabr.ru/company/jugru/blog/280420/  
https://habrahabr.ru/post/326242/  
https://codeahoy.com/2017/08/06/basics-of-java-garbage-collection/  


https://www.excelsiorjet.com/blog/articles/portable-profilers-and-where-to-find-them/

 

### The Various Kinds of IO - Blocking, Non-blocking, Multiplexed and Async 
https://www.rubberducking.com/2018/05/the-various-kinds-of-io-blocking-non.html
https://news.ycombinator.com/item?id=17009547

#### In Hardware 
On modern operating systems, IO, for input/output, is a way for data to be exchanged with peripherals. 
This includes reading or writing to disk, or SSD, sending or receiving data over the network, displaying data to the monitor, 
receiving keyboard and mouse input, etc.

The ways in which modern operating systems communicate with peripherals depends on the specific type of peripherals 
and their firmware and hardware capabilities. In general, you can assume that the peripherals are quite advanced, 
and they can handle multiple concurrent requests to write or read data. 
That is, gone are the days of serial communication. 
In that sense, all communications between the CPU and peripherals is therefore asynchronous at a hardware level.

This asynchronous mechanism is called hardware interrupt. 
Think of the simple case, where the CPU would ask the peripheral to read something, and it would then go in an infinite loop,
where each time it would check with the peripheral if the data is now available for it to consume, 
looping until the peripheral gives it the data. This method is known as polling, since the CPU needs to keep checking on the peripheral. 
On modern hardware, what happens instead is that the CPU asks the peripheral to perform an action, and then forgets about it, 
continuing to process other CPU instructions. Once the peripheral is done, it will signal the CPU through a circuit interrupt. 
This happens in hardware, and makes it so the CPU never waits or checks on the peripheral, thus freeing it to perform other work,
until the peripheral itself says it's done.

#### In Software 
So now that we have an understanding of what happens in hardware, we can move on to the software side. 
This is where the IO is exposed in various kinds, such as blocking, non-blocking, multiplexed and async. Lets go over them one by one.

#### Blocking
Remember how a user program runs inside a process, and code is executed within the context of a thread? 
This is always the case, and thus say you are writing a program that needs to read from a file.
With blocking IO, what you do is ask the operating system, from your thread, to put your thread to sleep, 
and wake it up only once the data from the file is available to be consumed by your thread.

That is, blocking IO is called blocking because the thread which uses it will block and sleep until the IO is done.

#### Non-blocking
The problem with blocking IO is that your thread is sleeping until the IO is done, and thus, 
it can't do anything else while it's waiting for the IO. 
Sometimes, there's nothing else your program could be doing, but if there was, it would be nice to be able to do that work concurrently,
as it waits for the IO.

One way to do that is with was is called non-blocking IO. The idea is that when you make the call to read the file, 
instead of putting your thread to sleep, the OS simply returns to you either the file's content that it read, 
or a pending status that tells you the IO is not done. 
It will not block your thread, but it's still your job to check back at a later time to see if the IO is done. 
This means you are free to branch on the pending status, and go perform some other work, and when you need the IO again, 
you can call read for it once more, at which point if the IO is done, it will return the file's content, 
otherwise it will once again return a pending status, and you can again choose to go perform some other work.

#### Multiplexed
The problem with non-blocking IO is that it gets strange if the other work that you want to be doing while waiting for the IO 
is itself more IO.

In a good scenario, you ask the OS to read content from file A, and then you go perform some heavy computation, 
once you're done, you check if file A is done reading, if so, you do whatever you needed that file's content for, 
otherwise, you go do some more heavy processing, rinse and repeat. 
But in the bad scenario, you don't have heavy processing to do, in fact, you want to read file A, and you also want to read file B. 
So while you wait for file A's IO, you make a non-blocking call to read file B's. Now what will you do while waiting for both? 
There's nothing for you left to do, so your program has to go into an infinite polling loop, where you keep checking if A is done,
and then if B is done, over and over. This will either consume the CPU simply to poll for the status of your non-blocking IO calls,
or you'll have to manually add some arbitrary sleep time, meaning that you'll probably realize the IO is ready a little after it
really was, slowing your program's throughput.

To avoid this problem, you can use multiplexed IO instead. What this does is that you will once again block on the IO,
but instead of blocking on a single IO operation to be done and then the other,
you are able to queue up all the IO operations you need done, and then block on all of them.
The OS will wake you up when any one of them is done. Some implementations of multiplexed IO allow even more control, 
where you can specify that you want to be woken up only if some specified set of IO operations are done,
like when file A and C or file B and D are done.

So you would make a non-blocking call to read file A, and then a non-blocking call to read file B, 
and finally you will tell the OS, put my thread to sleep, and wake it up when A and B's IO are both done, 
or when anyone of them is done.

#### Async
The problem with multiplexed IO is that you're still sleeping until IO is ready for you to handle. Once again, 
for many program that's fine, maybe you have nothing else to be doing while you wait for IO operations to be done. 
Sometimes though, you do have other things you could be doing. Maybe you're computing the digits of PI, 
while also summing up the values in a bunch of files. What you'd like to do is queue up all your file reads,
and while you wait for them to be read, you would compute digits of PI. When a file is done reading,
you'd sum up its values, and then go back to computing more digits of PI until another file is done reading.

For this to work, you will need a way for your digits of PI computation to be interrupted by the IO as it completes, 
and you'd need the IO to perform the interrupt when it completes.

This is done through event callbacks. The call to perform a read takes a callback, and returns immediately. 
On the IO completing, the OS will suspend your thread, and execute your callback. Once the callback is done executing, 
it will resume your thread.

Multi-threaded vs Single Threaded?
You'd have noticed that all kinds of IO that I described only speak of one single thread, which is your main application thread. 
The truth is, IO does not require a thread to be performed, because as I explained in the beginning, 
the peripherals all perform the IO asynchronously within their own circuitry. 
Thus it's possible to do blocking, non-blocking, multiplexed and async IO all within a single threaded model.
Which is why concurrent IO can work without multi-threaded support.

Now, the processing that is done on the result of the IO operations, or which is requesting the IO operations can obviously
be multi-threaded if you need it to be. This allows you to have concurrent computation on top of concurrent IO. 
So nothing prevents mixing multi-threaded and these IO mechanisms.

In fact, there is a very popular fifth kind of IO which does depend on multi-threading.
It is often confusingly referred to as non-blocking IO or async IO also, because it presents itself with a similar interface 
as one or the other. In truth, it is faking true non-blocking or async IO. 
The way it works is simple, it uses blocking IO, but each blocking call is made in its own thread.
Now depending on the implementation, it either takes a callback, or uses a polling model, like returning a Future.



Further Reading
non-blocking IO vs async IO and implementation in Java
Asynchronous and non-blocking IO
Multiplexed I/O
Reactor pattern
Proactor pattern
There is no thread

https://habr.com/ru/companies/oleg-bunin/articles/571116/

https://habr.com/ru/articles/328170/
```python
class Profiler(object): #профилировщик времени
    def __init__(self,info=''):
        self.info = info
    def __enter__(self):
        self._startTime = time()
    def __exit__(self, type, value, traceback):
        print(self.info, "Elapsed time: {:.3f} sec".format(time() - self._startTime))

Поехали… Для чистоты эксперимента введем num_iter = 1000 — число испытаний.

Протестируем профилировщик на чтении формулы-строки из файла:

with Profiler('read (' + str(num_iter) + '): cycle'):
    for i in range(num_iter):
        f = open('expr.txt')
        expr_txt = f.read()
        f.close()
```

https://habr.com/ru/companies/selectel/articles/450818/
There are a lot of tools for debugging kernel and userspace programs in Linux. Most of them have performance impact and cannot easily be run in production environments. 
A few years ago, eBPF was developed, https://lwn.net/Articles/740157/
which provides the ability to trace the kernel and userspace with low overhead
        
https://habr.com/ru/companies/microsoft/articles/271547/ Анализ ключевых показателей производительности — часть 1

https://habr.com/ru/companies/vk/articles/109916/  Видео с HighLoad++: Joe Damato — Performance tweaks and tools for Linux  
https://habr.com/ru/companies/galssoftware/articles/543314/  Appdynamics, Dynatrace и New Relic   
https://habr.com/ru/articles/505108/ Linux tuning to improve PostgreSQL performance. Илья Космодемьянский  
https://habr.com/ru/articles/600123/ Kernel Queue: The Complete Guide On The Most Essential Technology For High-Performance I/O  
https://habr.com/ru/articles/469409/ Профилирование под Linux с помощью Performance Analyzer  
https://habr.com/ru/companies/postgrespro/articles/902088/  Профессия performance инженер: детектив с лицензией на производительность   
https://habr.com/ru/companies/microsoft/articles/276549/  Query Performance Insight: кто ест ресурсы вашей базы данных? Azure SQL Database  

https://habr.com/ru/articles/157997/  О тонкостях повышения performance на С++, или как делать не надо  

 https://habr.com/ru/articles/326242/ Java  
 https://habr.com/ru/companies/jugru/articles/320620/  мониторинг производительности JVM под Linux при помощи BPF  
 https://habr.com/ru/companies/jugru/articles/338928/ В поисках перформанса, часть 2: Профилирование Java под Linux  
 https://habr.com/ru/articles/542156/  

 https://habr.com/ru/articles/412767/ кэшей, CDN, настройки правильного разрешения изображений, использования компрессии. А главное тестирования того, что получилось, как оказалось многие думают, что используют кэш, но порядка 70% контента при этом может не кэшироваться из-за неверных настроек.

https://habr.com/ru/companies/microsoft/articles/282740/ Анализ производительности Windows
 https://habr.com/ru/articles/564020/  Подводные камни сбора метрик в Windows (часть 1)

 https://habr.com/ru/companies/tbank/articles/670768/ Gatling работу с HTTP, JDBC, gRPC и Kafka  

http://www.brendangregg.com/sysperfbook.html

 https://habr.com/ru/articles/328362/ memory barriers, atomic operations

 https://www.drdobbs.com/parallel/volatile-vs-volatile/212701484  volatile vs. volatile
