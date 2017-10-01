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
      bool add(int key, E e); // pass by reference?
      void clear(){ entries.clear();};
      bool hasTag(int tagId);
      int countTag();
      void display_all();
      void display(int key);
      size_t size() { return entries.size();};
      bool removeByKey(int key);
      int removeByTag(int tagId);   //return # of removed items??    shrink_to_fit method.
   private:
      size_t _capacity;
      unordered_map<int, E> entries;   //syncronized   lock guard
};


bool Cache::add(int key, E e) {
   if  (entries.size() == _capacity) //better policy - LRU cache
     return false;
   // thread safe
   auto result = entries.insert({key,e});
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



void Cache::display_all() {
      cout << "======Display all===" << endl;
      for (std::pair<int, E> e: entries){
        display(e.first);
      }
}

int Cache::removeByTag(int tag) {
       cout << "======removeByTag() tag=" << tag << endl;
       auto it = entries.begin();

       while (it != entries.end()){
          if (  (it->second).tags.find(tag) != (it->second).tags.end() )
            entries.erase(it++);
          else
             ++it;
       }
      return 0;
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
     for (int i=1; i < 9; ++i) {
        key=i;
        e.value=i*10;
        e.tags={i*2, i*3};
        result = c.add(key, e);
        cout << "Key=" << key << "  Insert result=" << result << endl;
     }
     pair<E, bool> p = c.get(1);
     if (p.second) { cout << " found entry for key 1\n" ; }
     else  { cout << " NOT found entry for key 1\n" ; }

     p = c.get(10);
     if (p.second) { cout << " found entry for key 10\n"; }
     else  { cout << " NOT found entry for key 10\n" ; }


     c.display_all();
     cout << " BEFORE REMOVE N# of elements=" << c.size() << endl;
     c.removeByTag(6);
     cout << " AFTER REMOVE N# of elements=" << c.size() << endl;
     c.display_all();
     return 0;
}