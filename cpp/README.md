https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md

clang++ -Wall -std=c++11 boolean_matrix.cpp -o test

g++ -std=c++11 boolean_matrix.cpp

A derived class constructor always calls a base class constructor.


https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)

https://msdn.microsoft.com/en-us/library/s16xw1a8.aspx

http://thispointer.com/map-vs-unordered_map-when-to-choose-one-over-another/

https://codeofconnor.wordpress.com/2017/09/12/pass-by-reference-vs-pass-by-value-in-cpp/

http://thispointer.com/using-unordered_set-with-custom-hasher-and-comparision-function/


* STL container: How to avoid the temporary object creation

https://stackoverflow.com/questions/20487801/how-to-store-objects-without-copy-or-move-constructor-in-stdvector

https://stackoverflow.com/questions/19826376/insert-into-vector-having-objects-without-copy-constructor


for certain functions, like vector<T>::push_back using move constructors/assignments of T instead of copy constructors/assignments can dramatically increase performance.

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
