// g++ -std=c++11 reverse_words.cpp

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <iterator>
using namespace std;

#include <stdio.h>
#include <stdlib.h>

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


    map <int, std::string> mapOfPlanets;
    mapOfPlanets.insert(make_pair(1,"earth"));
    mapOfPlanets.insert(make_pair(2,"moon"));
    mapOfPlanets.insert(make_pair(3,"earth"));
    vector<int> keys;
    bool result = findByValue(keys, mapOfPlanets, std::string("earth"));
    for(auto& i : keys)
        std::cout << i << '\n';
    //cout << keys;
}
