https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md

clang++ -Wall -std=c++11 boolean_matrix.cpp -o test

g++ -std=c++11 boolean_matrix.cpp

A derived class constructor always calls a base class constructor.


<https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)>

A [link] https://msdn.microsoft.com/en-us/library/s16xw1a8.aspx

A [link]http://thispointer.com/map-vs-unordered_map-when-to-choose-one-over-another/

A [link] https://codeofconnor.wordpress.com/2017/09/12/pass-by-reference-vs-pass-by-value-in-cpp/

A [link] http://thispointer.com/using-unordered_set-with-custom-hasher-and-comparision-function/

class Rectangle {
  public:
    Rectangle(int width, int length) : m_width(width), m_length(length)
    {}
    int Size() {return m_width * m_length ; }
  private:
    int m_width;
    int m_length;
};
