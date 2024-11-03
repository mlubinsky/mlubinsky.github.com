https://habr.com/ru/companies/otus/articles/833462/

https://habr.com/ru/companies/wunderfund/articles/843618/

https://piotrminkowski.com/2022/01/05/useful-unknown-java-features/

https://www.youtube.com/watch?v=t03DOhiTPkc

Modern Java in Action
https://www.youtube.com/watch?v=miUbs3mqPJE

https://habr.com/ru/articles/806027/  Java for interview

https://habr.com/ru/companies/otus/articles/843394/ Memory Fences и volatile в Java: низкоуровневые гарантии порядка памяти
 
 http://whichjdk.com/

 https://sdkman.io/install
 
 What is a modern Java environment?
 https://news.ycombinator.com/item?id=30841581

https://www.ej-technologies.com/jprofiler 

https://nipafx.dev/java-visitor-pattern-pointless/


 ### Modern Java/JVM build practises

 https://habr.com/ru/articles/789344/ Maven

 https://github.com/binkley/modern-java-practices

 https://news.ycombinator.com/item?id=38875318
 
 
 ### Java from command line:
 https://habr.com/ru/post/652985/
 
 
 https://evacchi.github.io/java/records/jbang/2021/10/12/learn-you-an-actor-system-java-17-switch-expressions.html
 
 <https://www.amazon.com/Effective-Java-Joshua-Bloch/dp/0134685997> Effective Java 3rd ed Joshua Bloch

https://habr.com/ru/articles/739338/ JVM Internals

### Java Interview questions

https://dzone.com/articles/top-40-java-8-interview-questions-with-answers

https://habr.com/ru/articles/743862/  

https://habr.com/ru/articles/745910/
 
 Java in 2021
 https://www.avanwyk.com/revisiting-java-in-2021-ii/
 
 https://news.ycombinator.com/item?id=28584518
 
 <https://pro-prof.com/archives/7527>
 
 <https://medium.com/@leventov/smoothiemap-2-the-lowest-memory-hash-table-ever-6bebd06780a3> .   Hash Tables comparisons
 
 <https://advancedweb.hu/a-categorized-list-of-all-java-and-jvm-features-since-jdk-8-to-14/>
 
 https://advancedweb.hu/new-language-features-since-java-8-to-17/
 
 https://habr.com/ru/post/551492/ . what is new in Java
 
### looping over string chars
```
List<Integer> numbers = new ArrayList<>();
 
for (char c : myString.toCharArray()) {

}
 ```
 
### Reverse string without using reverse()
``` 
for(int i=s.length();i>0;--i)                //i is the length of the string  
{  
System.out.print(s.charAt(i-1));            //printing the character at index i-1  
} 
```
 
 
 ### Maven
``` 
 Source code goes in src/main/java. 
 Test code goes in src/test/java, 
 Resources (images, files, whatever) go in src/main/resources, 
 Test resources go in src/test/resources. 
 There is a pom.xml file that contains dependencies, and if it doesn't, it points to a parent which <<does>> contain them.

 There might be submodules and they all are folders containing another pom.xml. 
 That pom.xml generally points to the main pom.xml.
 ```

 ## JVM 

 https://habr.com/ru/companies/otus/articles/776342/  Garbage collection
 
 https://habr.com/ru/post/685518/

 https://habr.com/ru/companies/otus/articles/756450/

 https://itnext.io/the-memory-structure-of-jvm-part-2-d103426369c2
 
 https://habr.com/ru/post/560984/ memory /cpu usage
 
 https://habr.com/ru/post/556268/ . Memory
 
 https://habr.com/ru/company/mailru/blog/559794/
 
 https://habr.com/ru/post/549176/
 
 https://habr.com/ru/post/536288/ Java HotSpot JIT компилятор — устройство, мониторинг и настройка (часть 1)
 
 <https://habr.com/ru/post/471772/> How Java works
 
 <https://habr.com/ru/company/otus/blog/478584/> . JVM internals
 
 <https://habr.com/ru/company/domclick/blog/500646/> Java bytecode internals
 
 <https://www.youtube.com/watch?v=RtHA1YVLW5Y> JVM does this?
 
  <https://habr.com/ru/post/510618/> Java Memory Model
 
 https://medium.com/javarevisited/java-concurrency-java-memory-model-96e3ac36ec6b Java Memory Model
 
https://habr.com/ru/companies/otus/articles/843394/  Memory Fences и volatile в Java: низкоуровневые гарантии порядка памяти

 
 <https://www.youtube.com/watch?v=yhguOt863nw>. Java concurrency
 
 <https://www.baeldung.com/>
 
 <https://jokerconf.com/2019/talks/> . Java Conf
 
 <https://youtu.be/qurG_J81_Cs> Pattern matching
 
 <https://habr.com/ru/post/479478/> . каркас приложения на Java >9 с поддержкой динамической загрузки плагинов 
 
 An executable JAR is a just regular archive, with an included META-INF/manifest file 
 that says which "main" class should be the entry point. 
 The JRE knows to look for this manifest file.
 
 Run with the parameter:
 
 java.exe -jar  name.jar
 
 ## JDBC etc
 
 https://www.marcobehler.com/guides/java-databases-jdbc-hibernate-spring-data
 
 ## Promises vs Observables
 Both Promises and Observables will help us work with the asynchronous functionalities in JavaScript.

The main differences between them are listed below:
```
Promise:
Promises are values that will resolve in asynchronous ways like http calls
They have one pipeline
They are usually only use with async data return
They are not easy to cancel

Observable:

Observables deal with a sequence of asynchronous events
They are cancellable
They are retriable by nature such as retry and retryWhen
They stream data in multiple pipelines
They have array-like operations like map, filter etc.
They can be created from other sources like events
They are functions, which could be subscribed later on
```

From here: <https://habr.com/ru/company/piter/blog/466529/>
Чтобы байт-код Java выполнял какую-либо конкретную работу, есть 3 возможности заставить его это сделать:

* Непосредственно выполнить промежуточный код. Лучше и правильнее сказать, что его нужно «интерпретировать». В JVM есть интерпретатор языка Java. Как вы знаете, для работы JVM нужно запустить программу “java”.

* Непосредственно перед выполнением промежуточного кода скомпилировать его в нативный код и заставить CPU выполнить этот свежеиспеченный нативный код. Таким образом, компиляция происходит прямо перед выполнением (Just in Time) и называется «динамической».

* Самым первым делом, еще до запуска программы, промежуточный код переводится в нативный и прогнать его через CPU с начала до конца. Такая компиляция производится перед выполнением и называется AoT (Ahead of Time).


Итак, (1) – это работа интерпретатора, (2) — результат JIT-компиляции и (3) — результат AOT-компиляции.

Ради полноты картины упомяну, что существует и четвертый подход – напрямую интерпретировать исходный код, но в Java так не принято. Так делается, например, в Python.

Теперь давайте разберемся, как “java” работает в качестве (1) интерпретатора (2) JIT-компилятора и/или (3) AOT-компилятора – и когда.

Если коротко – как правило, “java” делает и (1), и (2). Начиная с Java 9 возможен и третий вариант. 



### HashMap. ConcurrentHashMap

https://stackoverflow.com/questions/1291836/concurrenthashmap-vs-synchronized-hashmap

```
We should favor Collections.synchronizedMap() when data consistency is of utmost importance,
and we should choose ConcurrentHashMap for performance-critical applications where there are far more write operations than there are read operations.

This is because the Collections.synchronizedMap() requires each thread to acquire a lock on the entire object for both read/write operations. 
By comparison, the ConcurrentHashMap allows threads to acquire locks on separate segments of the collection, and make modifications at the same time.

Hashtable is belongs to the Collection framework; ConcurrentHashMap belongs to the Executor framework. Hashtable uses single lock for whole data. ConcurrentHashMap uses multiple locks on segment level (16 by default) instead of object level i.e. whole Map . ConcurrentHashMap locking is applied only for updates
```

### Interfaces
```
import java.io.*;
 
// A simple interface
interface In1 {
   
    // public, static and final
    final int a = 10;
 
    // public and abstract
    void display();
}
 
// A class that implements the interface.
class TestClass implements In1 {
   
    // Implementing the capabilities of interface
    @Override
    public void display(){
      System.out.println("Geek");
    }
 
    // Driver Code
    public static void main(String[] args)
    {
        TestClass t = new TestClass();
        t.display();
        System.out.println(a);
    }
}
```


