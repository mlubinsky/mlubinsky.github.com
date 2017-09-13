https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md

clang++ -Wall -std=c++11 boolean_matrix.cpp -o test
g++ -std=c++11 boolean_matrix.cpp
clang++ -std=c++11 boolean_matrix.cpp


https://msdn.microsoft.com/en-us/library/s16xw1a8.aspx
A derived class constructor always calls a base class constructor.

https://codeofconnor.wordpress.com/2017/09/12/pass-by-reference-vs-pass-by-value-in-cpp/

class Rectangle {
  public:
    Rectangle(int width, int length) : m_width(width), m_length(length)
    {}
    int Size() {return m_width * m_length ; }
  private:
    int m_width;
    int m_length;
};
