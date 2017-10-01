#include <iostream>
#include <unordered_set>
#include <unordered_map>

#include <algorithm>
#include <thread>

using namespace std;


class E {
public:
   int value;
   unordered_set<int> tags;   // O(1) if no collision ; O(n) in worst case
};

class Cache {
  public:
      Cache(size_t capacity) : _capacity(capacity) { entries.reserve(capacity); cout << "Constructor"<< endl; };
     ~Cache() {  cout << "Destructor"<< endl;  };

      bool exist(int key);
      pair<E, bool>  get(int key);   // by value of by reference?
      bool add(int key, E e, unordered_set<int> tags); // pass by reference?
      void clear(){ entries.clear();};
      bool hasTag(int tagId);

      void display_all();
      void display_tags();
      void display(int key);
      size_t size() { return entries.size();};
      bool removeByKey(int key);
      bool removeByTag(int tagId);   //return # of removed items??    shrink_to_fit method.
   private:
      size_t _capacity;
      unordered_map<int, E> entries;   //syncronized   lock guard
      //unordered_map<int, unordered_set<int> > tags1;
      unordered_multimap<int, int> tags2;
};


bool Cache::add(int key, E e, unordered_set<int> tags) {
   if  (entries.size() == _capacity) //better policy - LRU cache
     return false;
   // thread safe
   auto result = entries.insert({key,e});
   if (result.second) {
        for (auto tag : tags)
           tags2.insert({tag,key});

   }
   return result.second;
}


void Cache::display(int key) {

  cout << "----Display entry:  key=" << key ;
  auto it = entries.find(key);

  if (it != entries.end()) {
      cout <<  " Value="<< entries[key].value ;

      cout << "  TAGS: " ;
      for ( auto item:  entries[key].tags) {
          cout << item << " ";
      }
      cout << endl;
   } else {
      cout << "No entry for Key="<< key << endl;
   }

}


void Cache::display_tags() {
      cout << "======Display tags===" << endl;
      for (auto t: tags2){
        cout <<"Tag=" << t.first << "  key="<< t.second << endl; ;
      }
}



void Cache::display_all() {
      cout << "======Display all  size="  << size() << endl;
      for (std::pair<int, E> e: entries){
        display(e.first);
      }
}


bool Cache::removeByTag(int tag) {
    cout << "======removeByTag() tag=" << tag << endl;
    auto ret = tags2.equal_range(tag);

    //for (std::multimap<char,int>::iterator it=ret.first; it!=ret.second; ++it)
    for (auto it=ret.first; it!=ret.second; ++it){
       cout << " KEY TO BE REMOVED= " << it->second  << endl;
       entries.erase(it->second );
    }
    tags2.erase(ret.first, ret.second);
    return true;
}



std::pair<E, bool> Cache::get(int key) {

  cout << "----get()  for key=" << key ;
  auto it = entries.find(key);

  if (it != entries.end()) {
      return std::make_pair(it->second, true);

   } else {

      return std::make_pair(E(), false);
   }

}


int main ( int argc,  char** argv) {

     Cache c(5);   //capacity as argument

     int key;
     E e;
     bool result;
     unordered_set<int> tags;

     for (int i=1; i < 9; ++i) {
        key=i;
        e.value=i*10;
        e.tags={i*2, i*3};
        tags.clear();
        tags.insert(i*2);
        tags.insert(i*3);
        result = c.add(key, e, tags);
        cout << "Key=" << key << "  Insert result=" << result << endl;
     }
     pair<E, bool> p = c.get(1);
     if (p.second) { cout << " found entry for key 1\n" ; }
     else  { cout << " NOT found entry for key 1\n" ; }

     p = c.get(10);
     if (p.second) { cout << " found entry for key 10\n"; }
     else  { cout << " NOT found entry for key 10\n" ; }


     c.display_all();
     c.display_tags();

     cout << " BEFORE REMOVE N# of elements=" << c.size() << endl;
     c.removeByTag(6);
     cout << " AFTER REMOVE N# of elements=" << c.size() << endl;
     c.display_all();
     c.display_tags();
     return 0;
}