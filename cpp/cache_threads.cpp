#include <iostream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <thread>
#include <mutex>

using namespace std;
/*
 TCache  class stores (key, values) pairs.
 The cache capacity shall be passed to constructor.
 When cach is full the new entries cannot be added (it is not LRU cache).
 TCache is thread-safe.
 For every key the list of tags may be specified (optionally)
 Supported operations:
 get() -  O(1)
 add() -  O(1)
 removeByKey() -  O(1)
 removeByTag() -   proportional to number of elements  with given tag
*/
template <typename Key, typename Val, typename Tag>
class TCache {
  public:

      TCache() = delete; //because no default cache size

      TCache(size_t capacity) : _capacity(capacity) {
          _entries.reserve(capacity);
      };

      ~TCache() { };

      /*---------------------------------------------------*/
      pair<Val, bool> get(Key key) {
        lock_guard<recursive_mutex> guard(_mutex);

        auto it = _entries.find(key);
        if (it != _entries.end()) {
            return make_pair(it->second, true);
        } else {
            return make_pair(Val(), false);
        }
      }

      /*---------------------------------------------------*/
      bool add(Key key, Val val, unordered_set<Tag>& tags) {
           lock_guard<recursive_mutex> guard(_mutex);

           if  (_entries.size() == _capacity)
             return false;   // better policy would be LRU cache based on timestamp

           auto result = _entries.insert({key,val});
           if (result.second) {
               for (auto t : tags){

                       auto it = _tag2key.find(t);
                       if (it != _tag2key.end()) {
                         _tag2key[t].insert(key);
                       } else {  // new tag
                         _tag2key.insert({t,  (unordered_set<Key>){key} });
                       }

                       _key2tag[key].insert(tags.begin(), tags.end());

               }
           }
           return result.second;
      }

    /*---------------------------------------------------*/
     bool removeByKey(Key key) {
        lock_guard<recursive_mutex> guard(_mutex);

        auto it = _key2tag.find(key);
        if (it != _key2tag.end()) {

             for (auto tag: it->second){
                  _tag2key[tag].erase(key);

                  if (_tag2key[tag].empty()) {
                    _tag2key.erase(tag);
                  }
             }
        }

        _key2tag.erase(key);
        _entries.erase(key);
        return true;
     }

     /*---------------------------------------------------*/
      bool removeByTag(Tag tag) {
          lock_guard<recursive_mutex> guard(_mutex);

          auto it = _tag2key.find(tag);

          if (it == _tag2key.end())
            return false;

          vector<Key> keys;
          for (auto key: it->second){
                   keys.push_back(key);
          }

          for (auto key : keys){
             removeByKey(key);
          }

          return true;
      }

      /*---------------------------------------------------*/
      void display(Key key) {
          lock_guard<recursive_mutex> guard(_mutex);

          cout << " Display one entry:  key=" << key ;
          auto it = _entries.find(key);
          if (it != _entries.end()) {
              cout <<  " value="<< _entries[key] <<endl ;
           } else {
              cout << "No entry for Key="<< key << endl;
           }

           cout <<  " Tags are: ";
           auto it2 = _key2tag.find(key);
           if (it2 != _key2tag.end()) {
                for (auto tag: it2->second){
                   cout << " " << tag;
                }
                cout  << endl;
           }

      }

      /*---------------------------------------------------*/
      void display_all() {
              lock_guard<recursive_mutex> guard(_mutex);
              cout << "======Display all entries.  Cache size="  << size() << endl;
              for (pair<Key, Val> e: _entries){
                display(e.first);
              }
      }

      /*---------------------------------------------------*/
      void display_tags() {
             lock_guard<recursive_mutex> guard(_mutex);
             cout << "======Display tags===" << endl;
             for (auto t: _tag2key){
                cout <<"Tag=" << t.first << "  keys=" ;
                for (auto key: t.second){
                   cout << " " << key;
                }
                cout  << endl;
             }
             cout  << endl;
      }

    /*---------------------------------------------------*/
      size_t size() {
         return _entries.size();
      };

    /*---------------------------------------------------*/
     void clear() {
        lock_guard<recursive_mutex> guard(_mutex);
        _entries.clear();
        _key2tag.clear();
        _entries.clear();
     }

   private:
      size_t _capacity;
      unordered_map<Key, Val> _entries;
      unordered_map<Tag, unordered_set<Key> > _tag2key;
      unordered_map<Key, unordered_set<Tag> > _key2tag;
      recursive_mutex _mutex;
};

// Next function to be called from thread
void func1(TCache<int,int, int> &cache)
{
     cout << "Entering thread 1" << endl;

     bool result;
     unordered_set<int> tags;

     //let have max key=9 to see how API handles the non-existing keys (I ddeclared cache size=5)
     for (int key=1; key < 9; ++key) {
        tags.clear();
        tags.insert(key*2);
        tags.insert(key*3);
        result = cache.add(key, 10*key, tags);
     }

     this_thread::sleep_for(chrono::seconds(1));

     for (int key=1; key < 9; ++key) {
        pair<int,bool> v = cache.get(key);
        /* Commented to avoid printing from the thread, keep it for demo purpose only
        if (v.second)
             cout << " found " << v.first;
        else
             cout << " not found ";
        */
     }

     this_thread::sleep_for(chrono::seconds(1));

     for (int tag=1; tag < 9; ++tag) {
        cache.removeByTag(tag);
     }
}

// Next function to be called from thread
void func2(TCache<int, int, int> &cache)
{
     cout << "Entering thread 2" << endl;
     bool result;

     for (int tag=1; tag < 9; ++tag) {
        cache.removeByTag(tag);
     }

     this_thread::sleep_for(chrono::seconds(1));

     for (int key=1; key < 9; ++key) {
        pair<int,bool> v = cache.get(key);
        /* Commendet in order do not print from the theead, I keep code here to show how to handle the get()
        if (v.second)
             cout << " found " << v.first;
        else
             cout << " not found ";
        */
     }

     this_thread::sleep_for(chrono::seconds(1));

     unordered_set<int> tags;
     for (int key=1; key < 9; ++key) {
        tags.clear();
        tags.insert(key*2);
        tags.insert(key*3);
        result = cache.add(key, 10*key, tags);
     }
}


void test_single_thread () {

    TCache<int,int, string> cache(5);   //create cache with capacity=5;  using  here integer for (keys, values) and  string for tags

    unordered_set<string> tags1({"2","3","4","5"});
    cache.add(1,10, tags1);


    unordered_set<string> tags2({"4","5","6","7"});
    cache.add(2,20, tags2);

    cache.display_all();
    cache.display_tags();

    cache.removeByTag("7");
    pair<int,bool> v = cache.get(1);

    if (v.second)
       cout << "Found entry for key = 1 value=" << v.first << endl;
     else
        cout << "Not found entry for key = 1 "<< endl;

    cache.display_all();
    cache.display_tags();

}

int main ( int argc,  char** argv) {
    test_single_thread();

    // test several threads working with sane cache
    TCache<int,int,int> cache(5);  //using integer keys, values and tags; cache capacity=5
    thread firstThread(func1, ref(cache));
    thread secondThread(func2, ref(cache));
    firstThread.join();
    secondThread.join();
    return 0;
}