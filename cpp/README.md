https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md

clang++ -Wall -std=c++11 boolean_matrix.cpp -o test

g++ -std=c++11 boolean_matrix.cpp


### Constructor

A derived class constructor always calls a base class constructor.

https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)

https://msdn.microsoft.com/en-us/library/s16xw1a8.aspx

 Disable Copy and Move :

            HashMap(const HashMap&) = delete;

            HashMap(HashMap&&) = delete;

            HashMap& operator=(const HashMap&) = delete;

            HashMap& operator=(HashMap&&) = delete;

https://codeofconnor.wordpress.com/2017/09/12/pass-by-reference-vs-pass-by-value-in-cpp/

### STL

http://thispointer.com/stl-tutorials-and-interview-questions/


### STL container: How to avoid the temporary object creation

https://stackoverflow.com/questions/20487801/how-to-store-objects-without-copy-or-move-constructor-in-stdvector

https://stackoverflow.com/questions/19826376/insert-into-vector-having-objects-without-copy-constructor

https://stackoverflow.com/questions/26446352/what-is-the-difference-between-unordered-map-emplace-and-unordered-map-ins

https://crascit.com/2016/08/15/avoiding-copies-and-moves-with-auto/

for certain functions, like vector<T>::push_back using move constructors/assignments of T instead of copy constructors/assignments can dramatically increase performance.

### auto

1. const auto&  - when the container items don’t need to be modified
2. auto&  - if they do need to allow modification in-place.
3. auto   -  use a bare auto if the loop body really needs a copy of the item so it can make local modifications without affecting the items being iterated over, or if the items are known to always be built in types like int, double, etc. which are trivially cheap to copy.

### set
http://thispointer.com/using-unordered_set-with-custom-hasher-and-comparision-function/


### map

http://thispointer.com/map-vs-unordered_map-when-to-choose-one-over-another/

https://github.com/kshk123/hashMap/blob/master/inc/

https://stackoverflow.com/questions/12033188/how-would-you-implement-your-own-reader-writer-lock-in-c11?rq=1

https://stackoverflow.com/questions/19915152/c11-multiple-read-and-one-write-thread-mutex


https://stackoverflow.com/questions/43309333/stdshared-mutex-with-stdshared-lock-is-reader-or-writer-preferring


Here is the usual way of doing insert/overwrite in map:

auto rv = map.insert(std::make_pair(key, value));
if (!rv.second)
    rv.first->second = value;

 std::map is usually implemented as a balanced binary tree (red/black tree) so both insert() and find() take O(log(n)) steps.
 Example: the container has a natural internal order and insertion must place the new items at their correct place. (that is why the keys must be in strict weak order).

std::unordered_map uses hashing, so the lookup is O(1) for the default-constructed map (ie when there is a single item in every bucket). Once collisions are allowed (ie when you have k items in each bucket), each lookup would be take O(k) steps.


### Threads

1. Semaphores
2. Atomic references
3. Monitors
4. Condition codes
5. Compare and swap

http://thispointer.com/c11-multithreading-tutorial-series/

https://baptiste-wicht.com/categories/c%2B%2B11-concurrency-tutorial.html

### Keywords: noexept delete final default override ...


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
