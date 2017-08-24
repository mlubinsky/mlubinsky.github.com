// g++ -std=c++11 reverse_words.cpp

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <iterator>
using namespace std;

#include <stdio.h>
#include <stdlib.h>
/*
Q: What is assignment operator?
A: Default assignment operator handles assigning one object to another of the same class.
Member to member copy (shallow copy)

All containers in the STL are parameterized with template arguments,
usually the last argument is called A or Allocator and defaults to std::allocator<...>
where ... represents the type of the value stored within the container.

The Allocator is a class that is used to provide memory and build/destroy the elements in this memory area.
It can allocate memory from a pool or directly from the heap, whichever you build the allocator from.
By default the std::allocator<T> is a simple wrapper around ::operator new and will thus allocate memory on the heap as you inferred.

The memory is allocated on demand, and is deallocated at the very least when the vector's destructor is called.
C++11 introduces shrink_to_fit to release memory sooner too. Finally, when the vector outgrow its current capacity, a new (larger) allocation is made,
the objects are moved to it, and the old allocation is released.

As will all local variables, the destructor is called when executed reaches the end of the scope it has been declared into.
So, before the function is exited, the vector destructor is called, and only afterward does the stack shrinks and control returns to the caller.
============
Base class object's pointer can invoke methods in derived class objects. You can also achieve polymorphism in C++
by function overloading and operator overloading.

Q: How do you know that your class needs a virtual destructor?
A: If your class has at least one virtual function, you should make a destructor for this class
virtual. This will allow you to delete a dynamic object through a caller to a base class object. If
the destructor is non-virtual, then wrong destructor will be invoked during deletion of the
dynamic object.
============
A: Inherits:
Every data member defined in the parent class (although such members may not always be accessible in the derived class!)
Every ordinary member function of the parent class (although such members may not always be
accessible in the derived class!)
The same initial data layout as the base class.
===========
Doesn't Inherit :
The base class's constructors and destructor.
The base class's assignment operator.
The base class's friends
====
Q: What are VTABLE and VPTR?
A: vtable is a table of function pointers. It is maintained per class.
vptr is a pointer to vtable. It is maintained per object (See this for an example).
Compiler adds additional code at two places to maintain and use vtable and vptr.

1) Code in every constructor. This code sets vptr of the object being created. This code sets vptr to point to vtable of the class.
2) Code with polymorphic function call (e.g. bp->show() in above code).
Wherever a polymorphic call is made, compiler inserts code to first look for vptr using base class pointer or reference
(In the above example, since pointed or referred object is of derived type, vptr of derived class is accessed).
Once vptr is fetched, vtable of derived class can be accessed. Using vtable, address of derived derived class function show() is accessed and called.
==========================
*/

bool isAnagram2(std::string str1, std::string str2)
{
    std::sort(str1.begin(), str1.end());
    std::sort(str2.begin(), str2.end());
    return str1==str2;
}

bool isAnagram(const std::string &str1, const std::string &str2)
{
    int frequencies[256];
    memset(frequencies, 0, 256);

    for (int i = 0; i < str1.length(); i++)
    {
        int bucket = (unsigned char) str1[i];
        frequencies[bucket]++;
    }
    for (int i = 0; i < str2.length(); i++)
    {
        int bucket = (unsigned char) str2[i];
        frequencies[bucket]--;
    }

    for (int i = 0; i < 256; i++)
    {
        if (frequencies[i] != 0)
            return false;
    }
    return true;
}





void reverse_words(string &input) {

	reverse(input.begin(), input.end());
	size_t start=0;
	size_t end;
	while ((end=input.find(" ",start)) != string::npos){
		reverse(input.begin()+start, input.begin()+end);
		start=end+1;
	}
	reverse(input.begin()+start, input.end());
}



/*
 * Generic implementation to search if a given value exists in a map or not.
 * Adds all the keys with given value in the vector
 */
template<typename K, typename V>
bool findByValue(vector<K> & vec, map<K, V> mapOfElemen, V value)
{
	bool bResult = false;
	auto it = mapOfElemen.begin();
	while(it != mapOfElemen.end())
	{
		if(it->second == value)	{
			bResult = true;
			vec.push_back(it->first);
		}
		it++;
	}
	return bResult;
}

int main()
{
    map<std::string, int> mapOfWords;
    mapOfWords.insert(make_pair("earth", 1));
    mapOfWords.insert(make_pair("moon", 2));
    mapOfWords["sun"] = 3;
    mapOfWords["earth"] = 4;
    map<string, int>::iterator it = mapOfWords.begin();
    while(it != mapOfWords.end()){
        cout<<it->first<<" :: "  <<it->second  <<endl;
        it++;
    }
    if(mapOfWords.insert(make_pair("earth", 1)).second == false)
    {
        cout<<"Element with key 'earth' not inserted because already existed"<<endl;
    }
    // Searching element in std::map by key.
    if(mapOfWords.find("sun") != mapOfWords.end())
        cout<<"word 'sun' found"<<endl;
    if(mapOfWords.find("mars") == mapOfWords.end())
        cout<<"word 'mars' not found" <<endl;


    cout << "show content of map" <<endl;
    for (it=mapOfWords.begin(); it!=mapOfWords.end(); ++it)
         cout << it->first << " => " << it->second << '\n';

    string key="sun";
    if (mapOfWords.count(key))   {  // key exists
        auto  iter = mapOfWords.find(key);
        if (iter != mapOfWords.end() ){
                 // key 2 exists, do something with iter->second (the value)
        }
    }



//Find the first element in v  between x and y. In C+11, the simplest and cleanest code is to use a standard algorithm.

   // C++98: write a naked loop (using std::find_if is impractically difficult)
   vector<int> v = {7,5,16,8};
   int x=15;
   int y=20;
   vector<int>::iterator i = v.begin(); // because we need to use i later
   for( ; i != v.end(); ++i ) {
    if( *i > x && *i < y ) break;
   }
   cout << "The first element in v  between x and y is: " << *i  <<endl;;
   // C++11: use std::find_if
   //  find() If no matches were found, the function returns string::npos.
    auto ii = find_if( begin(v), end(v), [=](int i) { return i > x && i < y; } );
    cout << "The first element in v  between x and y is: " << *ii  <<endl;

    string s= "ABC DEF GH";
    cout << s  <<endl;
    reverse_words(s);
    cout << s << endl;


    cout << "IsAnagram? "<< isAnagram("ABD DD",  "DD DBC") << endl;
    cout << "IsAnagram? "<< isAnagram2("ABD DD", "DD DBC") << endl;

}
