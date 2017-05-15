#include <iostream>
#include <string>
#include <map>
#include <iterator>
using namespace std;

// find() If no matches were found, the function returns string::npos.

void reverse_words(string &input) {

	reverse(input.begin(), input.end());
	size_t start=0;
	site_t end;
	while ((end=input.find(" ",start)) != string.npos){
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
bool findByValue(std::vector<K> & vec, std::map<K, V> mapOfElemen, V value)
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
    std::map<std::string, int> mapOfWords;
    mapOfWords.insert(std::make_pair("earth", 1));
    mapOfWords.insert(std::make_pair("moon", 2));
    mapOfWords["sun"] = 3;
    mapOfWords["earth"] = 4;
    map<std::string, int>::iterator it = mapOfWords.begin();
    while(it != mapOfWords.end()){
        cout<<it->first<<" :: "<<it->second<<endl;
        it++;
    }
    if(mapOfWords.insert(std::make_pair("earth", 1)).second == false)
    {
        cout<<"Element with key 'earth' not inserted because already existed"<<endl;
    }
    // Searching element in std::map by key.
    if(mapOfWords.find("sun") != mapOfWords.end())
        cout<<"word 'sun' found"<<endl;
    if(mapOfWords.find("mars") == mapOfWords.end())
        cout<<"word 'mars' not found"<<endl;


  // show content:
    for (it=mymap.begin(); it!=mymap.end(); ++it)
         cout << it->first << " => " << it->second << '\n';


    if (m.count(key))  ....   // key exists
    auto  iter = m.find(2);
    if (iter != m.end() ){
    // key 2 exists, do something with iter->second (the value)
    }
}


    return 0;
}