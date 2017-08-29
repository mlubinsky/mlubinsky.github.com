

clang++ -Wall -std=c++11 boolean_matrix.cpp -o test
g++ -std=c++11 boolean_matrix.cpp
clang++ -std=c++11 boolean_matrix.cpp


https://msdn.microsoft.com/en-us/library/s16xw1a8.aspx
A derived class constructor always calls a base class constructor,
// member init list
===================
class Box {
public:
    Box(int width, int length, int height) : m_width(width), m_length(length), m_height(height)
    {}
    int Volume() {return m_width * m_length * m_height; }
private:
    int m_width;
    int m_length;
    int m_height;

};
