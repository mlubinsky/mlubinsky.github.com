#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <thread>

using namespace std;

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
      bool remove(int key);
      bool hasTag(int tagId);
      int countTag();
      void display(int key);
      int flushByTag(int tagId);   //return # of removed items??    shrink_to_fit method.
   private:
      unordered_map<int, E> entries;   //syncronized   lock guard
};


bool Cache::add(int key, E e) {
   typedef unordered_map<int, E>::iterator it;
   pair< it , bool> result;
   result = entries.insert({key,e});
   return result.second;
}

void Cache::display(int id) {
  /*
  if (entries[i]) {
      cout << "Key="<<id<<" Value="<< entries[i].value << endl;

      cout << "TAGS" << endl;
      for ( auto item:  entries[i].tags) {
          cout << item << endl;
      }
   } else {
      cout << "No entry for Key="<< id< <endl;
   }
   */
}


int main ( int argc,  char** argv) {
     //Cache<Entry> c;
     Cache c;

     E e;
     e.value=1;
     e.tags.insert(1);
     e.tags.insert(2);
     c.add(1,e);
     c.display(1);
     return 0;
}