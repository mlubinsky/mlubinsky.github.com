#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <thread>

using namespace std;

//entry shall be  the pair(). not the Class below E
class E {
public:
  int value;
  // vector<int> tags;
  // or set<int>  tags
   unordered_set<int> tags;   // O(1) if no collision ; O(n) in worst case
};

//template<class T>
class Cache {
  public:
      Cache() {  cout << "Constructor"<< endl; };   // constructor;
     ~Cache() {  cout << "Destructor"<< endl;  };  // destructor;

      bool exist(int key);
      E  get(int key);   // by value of by reference?
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
      unordered_map<int, E> entries;   //syncronized   lock guard
};


bool Cache::add(int key, E e) {
   typedef unordered_map<int, E>::iterator it;
   pair< it , bool> result;
   result = entries.insert({key,e});
   return result.second;
}

void Cache::display_all() {
      cout << "======Display all===" << endl;
      for (std::pair<int, E> e: entries){
        //cout << e.first << " :: " << e.second.value << endl;
        display(e.first);
      }
}

int Cache::removeByTag(int tag) {
       cout << "======removeByTag() tag=" << tag << endl;
       std::unordered_map<int, E>::iterator it = entries.begin();
       while (it != entries.end()){
          if (  (it->second).tags.find(tag) != (it->second).tags.end() )
            entries.erase(it++);
          else
             ++it;
       }
      return 0;
}

void Cache::display(int key) {

  cout << "----Display entry for key=" << key <<  endl;

  std::unordered_map<int, E>::iterator it;
  it = entries.find(key);

  if (it != entries.end()) {
      cout << "Key="<<key<<" Value="<< entries[key].value << endl;

      cout << "TAGS" << endl;
      for ( auto item:  entries[key].tags) {
          cout << item << endl;
      }
   } else {
      cout << "No entry for Key="<< key << endl;
   }

}


int main ( int argc,  char** argv) {
     //Cache<Entry> c;
     Cache c;   //capacity as argument? reserve size of cache

     E e;

     e.value=22;
     e.tags.insert(100);
     e.tags.insert(200);

     auto res = c.add(1,e);
     cout << "Insert result=" << res << endl;


     res = c.add(1,e);
     cout << "Insert result=" << res << endl;


     e.value=33;
     e.tags.insert(133);
     e.tags.insert(233);
     res = c.add(2,e);

     e.value=33;
     e.tags.insert(500);
     res = c.add(3,e);

     //c.display(1);
     c.display_all();
     cout << "N# of elements=" << c.size() << endl;
     c.removeByTag(133);
     cout << "N# of elements=" << c.size() << endl;

     return 0;
}