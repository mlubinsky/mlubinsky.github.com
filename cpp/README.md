https://habr.com/ru/companies/ruvds/articles/871940/  .a .so, linking / building C/C++  

### Make, CMAke, etc
https://habr.com/ru/companies/ruvds/articles/875620/ Сборка проектов Си и Си++: от простого к сложному. Часть II

https://www.youtube.com/watch?v=gqczXq-faAg   CMake

https://coderefinery.github.io/cmake-workshop/motivation/ CMake

### Telegram
https://t.me/s/bfbook  https://t.me/s/bfbook?before=4869  
https://t.me/s/cpp_lib  


https://www.youtube.com/watch?v=Zb57p6KfN3M Работа с файлами, в десятки раз превышающими размер оперативки

### C

https://www.youtube.com/watch?v=9UIIMBqq1D4   : C tips

https://github.com/oz123/awesome-c

https://github.com/stclib/STC  containers for C

https://github.com/rurban/ctl containers for C

https://nullprogram.com/blog/2025/01/19/ Examples of quick hash tables and dynamic arrays in C


Book: C Interfaces and implementation  https://www.amazon.com/Interfaces-Implementations-Techniques-Creating-Reusable/dp/0201498413  
https://github.com/drh/cii



https://accu.org/bookreviews/2020/glassborow_1952/ Book "Effective C" Robert C. Seacord

https://modernc.gforge.inria.fr/   Book "Modern C" Jens Gustedt

https://news.ycombinator.com/item?id=25176531 favorits C tricks

https://github.com/tezc/sc.  common C libraries

<https://codeplea.com/embedding-files-in-c-programs>

<https://wordsandbuttons.online/SYTYKC.pdf> C

https://news.ycombinator.com/item?id=24361469 . Modern C

### CPP
https://awesomecpp.com/

https://cacm.acm.org/blogcacm/21st-century-c/ Straustrup
 
https://habr.com/ru/companies/timeweb/articles/842878/

https://www.thephysicsmill.com/2024/08/30/multi-dimensional-dynamically-sized-arrays-in-c-and-c-the-right-way/

https://habr.com/ru/articles/838392/

https://habr.com/ru/post/538954/ chain of responsibility and command design pattern

https://alexgaynor.net/2024/aug/18/safer-c-plus-plus/

https://habr.com/ru/post/545946/ embedding any file to c/c++

https://habr.com/ru/articles/822509/  Static and dynamic polymorfism

https://habr.com/ru/companies/pvs-studio/articles/822911/ arrays and poiner problems

https://habr.com/ru/companies/yandex_praktikum/articles/807387/  lot of cpp links

https://habr.com/ru/articles/831754/  1000 C++ libs

comparing hash implementations
https://jacksonallan.github.io/c_cpp_hash_tables_benchmark/

good C++ codebase
https://www.reddit.com/r/cpp/comments/1ef0yna/looking_for_examples_of_good_idiomatic_codelibs/

### Macros

while(0) in macro https://bowero.nl/blog/2020/10/25/defining-c-macros-the-right-way/

https://habr.com/ru/post/546946/

### Single file libraries

https://github.com/nothings/single_file_libs

https://github.com/p-ranav/awesome-hpp

https://habr.com/ru/company/pvs-studio/blog/524568/

<https://github.com/nothings/stb>

<https://github.com/nothings/single_file_libs>


### Memory allocators 

https://habr.com/ru/articles/876804/

<https://johnysswlab.com/the-price-of-dynamic-memory-allocation/> memory allocators

https://habr.com/ru/company/mailru/blog/525484/ memory allocators

https://news.ycombinator.com/item?id=42605848 Pull Allocator , Arena

https://habr.com/ru/articles/505632/ Аллокаторы памяти

https://habr.com/ru/companies/pvs-studio/articles/875922/

https://nullprogram.com/blog/2023/09/27/ arena memory allocator

https://nullprogram.com/blog/2024/05/25/

https://habr.com/ru/articles/876958/

### C++ static analysis

https://www.reddit.com/r/cpp/comments/ffx95k/static_analysis_tools_you_use_in_ci_for_your_cpp/   cpp static analysis

Using -D flag
gcc  -DDEBUG=1 d.c;
```
#include <stdio.h>
 
int main()
{
//    #ifdef DEBUG
#if DEBUG   == 1
       printf("Debug run=%d  \n", DEBUG);
#elif DEBUG ==2
printf("Debug run=%d  \n", DEBUG);
    #else
       printf("Release run\n");
    #endif

    return 1;
}
```

<https://medium.com/himinds/a-way-to-to-minimize-errors-and-make-your-c-code-easier-to-read-eb98ad6d3656>

```
printf(“%s %s:%d …”, __FILE__, __FUNCTION__, __LINE__, …);


char buf[100] = {0};   # same as memset(buf, 0, (sizeof(buf)/sizeof(buf[0]))) 
```

## Good C++ codebase to learn:

https://news.ycombinator.com/item?id=24901244


### ZigLang

<https://ziglang.org/> 

### Janet lang
<https://janet-lang.org/> 

<https://news.ycombinator.com/item?id=22975225>

### Gravity lang
<https://marcobambini.github.io/gravity/#/README>


## UI

<https://github.com/ocornut/imgui>  Dear ImGui 



<https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md>

<https://open.compscicenter.ru/archive/modern-cpp-1/>
<https://open.compscicenter.ru/archive/modern-cpp-2/>

<http://www.modernescpp.com/> 2 books here

<https://vk.com/for_programmer> russian cconferences Siberia 2019 C++


<https://lordsof.tech/tech/serialisation-of-c-classes-with-very-little-code/>. serialization


### Concurrent pthreads

<https://begriffs.com/posts/2020-03-23-concurrent-programming.html>

### LD_PRELOAD
<https://github.com/gaul/awesome-ld-preload>

<https://blog.jessfraz.com/post/ld_preload/> . LD_PRELOAD


<https://www.amazon.com/Advanced-Interview-Questions-Youll-Likely/dp/1946383708> C++ book

<http://www.icce.rug.nl/documents/cplusplus/>

```
#include <stdio.h>

float get_model_result(float* temp_value){
 printf ("--- inside the get_model_result ---\n");
 for (int i=0; i<10; i++){
    printf("%f\n",temp_value[i]);
 }
 return 0.1f;
}

int main(){
 printf("Hello\r\n");
 float temp_value[10];
 for (int i=0; i<10; i++){
    temp_value[i]=i+0.01;
    printf("%f\n",temp_value[i]);
 }
 float res=get_model_result(temp_value);

 return 0;
}
```

<https://ds9a.nl/articles/posts/cpp-2/>

<https://tests4geeks.com/cpp-interview-questions/>

<https://habrahabr.ru/post/182920/>

https://habr.com/users/dm_frox/posts/

<https://habr.com/company/pvs-studio/blog/418645/> Conference

<https://www.youtube.com/channel/UCifgOu6ARWbZ_dV29gss8xw> CPP rus conference 

<https://www.codeproject.com/Articles/1170503/The-Impossibly-Fast-Cplusplus-Delegates-Fixed>

clang++ -Wall -std=c++11 boolean_matrix.cpp -o test

g++ -std=c++11 boolean_matrix.cpp

<https://github.com/CppCon/CppCon2017>

<https://manybutfinite.com/post/anatomy-of-a-program-in-memory/>

<https://channel9.msdn.com/Events/Build/2013/4-329>  C++ performance

<https://blog.nelhage.com/post/three-kinds-of-leaks/>

<https://habr.com/company/pvs-studio/blog/414467/>

<https://github.com/simongog/sdsl-lite>

### Constructor

A derived class constructor always calls a base class constructor.

<https://habr.com/ru/post/445948/>

<https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)>

<https://msdn.microsoft.com/en-us/library/s16xw1a8.aspx>

 Disable Copy and Move :

            HashMap(const HashMap&) = delete;

            HashMap(HashMap&&) = delete;

            HashMap& operator=(const HashMap&) = delete;

            HashMap& operator=(HashMap&&) = delete;

<https://codeofconnor.wordpress.com/2017/09/12/pass-by-reference-vs-pass-by-value-in-cpp/>

#### Type erasure

https://blog.the-pans.com/type-erasure/

### Overload new and delete
https://habr.com/ru/post/490640/

### STL

<http://thispointer.com/stl-tutorials-and-interview-questions/>

<http://www.techiedelight.com/data-structures-and-algorithms-interview-questions-stl/>

<https://qualapps.blogspot.com/2010/07/safely-using-erase-in-stl.html>

### STL container: How to avoid the temporary object creation

https://stackoverflow.com/questions/20487801/how-to-store-objects-without-copy-or-move-constructor-in-stdvector

https://stackoverflow.com/questions/19826376/insert-into-vector-having-objects-without-copy-constructor

https://stackoverflow.com/questions/26446352/what-is-the-difference-between-unordered-map-emplace-and-unordered-map-ins

https://crascit.com/2016/08/15/avoiding-copies-and-moves-with-auto/

for certain functions, like vector<T>::push_back using move constructors/assignments of T instead of copy constructors/assignments
can dramatically increase performance.

### auto

1. const auto&  - when the container items don’t need to be modified
2. auto&  - if they do need to allow modification in-place.
3. auto   -  use a bare auto if the loop body really needs a copy of the item so it can make local modifications without affecting the items being iterated over, or if the items are known to always be built in types like int, double, etc. which are trivially cheap to copy.

### set
<http://thispointer.com/using-unordered_set-with-custom-hasher-and-comparision-function/>


### map

<http://thispointer.com/map-vs-unordered_map-when-to-choose-one-over-another/>

<http://thispointer.com/c11-unordered_map-erase-elements-while-iterating-in-a-loop/>

Here is the usual way of doing insert/overwrite in map:

auto rv = map.insert(std::make_pair(key, value));
if (!rv.second)
    rv.first->second = value;

 std::map is usually implemented as a balanced binary tree (red/black tree) so both insert() and find() take O(log(n)) steps.
 Example: the container has a natural internal order and insertion must place the new items at their correct place. (that is why the keys must be in strict weak order).

std::unordered_map uses hashing, so the lookup is O(1) for the default-constructed map (ie when there is a single item in every bucket). Once collisions are allowed (ie when you have k items in each bucket), each lookup would be take O(k) steps.

### Heap and priority queue
<https://www.fluentcpp.com/2018/03/20/heaps-and-priority-queues-in-c-part-3-queues-and-priority-queues/>

### Matrix

>https://habr.com/ru/post/359272/> Умножение матриц: эффективная реализация шаг за шагом
<https://news.ycombinator.com/item?id=17164737>

vector <vector <int> > grid (3, vector(4,0))    //  grid size: 3x4 initialized by 0

<https://gist.github.com/nadavrot/5b35d44e8ba3dd718e595e40184d03f0>

<http://cpptruths.blogspot.com/2011/10/multi-dimensional-arrays-in-c11.html>

<http://www.stroustrup.com/Programming/Matrix/Matrix.h>

<https://www.techsoftpl.com/matrix/index.php>

<https://github.com/lindahua/light-matrix>

<http://matrix.drque.net/>

<https://www.mrericsir.com/blog/technology/c-2d-generic-array-class/>

<https://hackernoon.com/c-investigation-arrays-vs-vectors-e9ba864468b6>

<https://www.youtube.com/watch?v=tJRGKR4_yAM>

https://www.codeproject.com/Articles/3613/A-generic-reusable-and-extendable-matrix-class

<https://stackoverflow.com/questions/10764961/c-matrix-class-template>

<https://codereview.stackexchange.com/questions/142815/generic-matrix-type-in-c>

### Memory managment:  shared_ptr  weak_ptr  unique_ptr

<https://habr.com/ru/post/473294/>

<https://habr.com/post/425837/>

<https://techtalk-test.intersec.com/2013/07/memory-part-1-memory-types/>

<https://techtalk-test.intersec.com/2013/07/memory-part-2-understanding-process-memory/>

<https://techtalk-test.intersec.com/2013/08/memory-part-3-managing-memory/>

<https://techtalk-test.intersec.com/2013/10/memory-part-4-intersecs-custom-allocators/>

<https://genbattle.bitbucket.io/blog/2016/02/06/Modern-C-Memory-Management-With-unique-ptr/>

### Threads

<https://habr.com/ru/company/jugru/blog/446562/>

1. Semaphores
2. Atomic references
3. Monitors
4. Condition codes
5. Compare and swap

<http://thispointer.com/c11-multithreading-tutorial-series/>

<https://www.codeproject.com/Articles/1177478/Thread-Wrapper-CPP>

http://thispointer.com/c11-multithreading-part-7-condition-variables-explained/

<https://habrahabr.ru/post/182626/>

<https://habrahabr.ru/post/328348/>

<https://habr.com/ru/post/443406/>

http://www.bogotobogo.com/cplusplus/multithreaded4_cplusplus11B.php

https://baptiste-wicht.com/categories/c%2B%2B11-concurrency-tutorial.html

https://stackoverflow.com/questions/27860685/how-to-make-a-multiple-read-single-write-lock-from-more-basic-synchronization-pr

https://github.com/kshk123/hashMap/blob/master/inc/

https://stackoverflow.com/questions/12033188/how-would-you-implement-your-own-reader-writer-lock-in-c11?rq=1

https://stackoverflow.com/questions/19915152/c11-multiple-read-and-one-write-thread-mutex

https://stackoverflow.com/questions/43309333/stdshared-mutex-with-stdshared-lock-is-reader-or-writer-preferring

https://www.codeproject.com/Articles/1183423/We-make-a-std-shared-mutex-times-faster

<http://www.acodersjourney.com/2017/08/top-20-cplusplus-multithreading-mistakes/>

### Serialization

https://www.gamedev.net/articles/programming/general-and-gameplay-programming/pupping-a-method-for-serializing-data-r4485/

https://eliasdaler.github.io/meta-stuff/

http://www.idryman.org/blog/2017/06/28/opic-a-memory-allocator-for-fast-serialization/

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.219.7269&rep=rep1&type=pdf   B-Tree


### Hash
http://www.idryman.org/blog/2017/05/03/writing-a-damn-fast-hash-table-with-tiny-memory-footprints/

### Debug  
https://techtalk.intersec.com/2018/03/improved-debugging-with-rr/

<http://jovislab.com/blog/?p=33>

### Keywords: noexept delete final default override mutable...

<http://www.geeksforgeeks.org/c-mutable-keyword/>

class A {

  public:

    A(int width, int length) : m_width(width), m_length(length) {}

    int Size() {return m_width * m_length ; }

    void f() noexcept;  // turns an exception throw into a call to std::terminate().

    A(const A&) = delete; /* to deny copy-construction */

  private:

    int m_width;

    int m_length;

};
