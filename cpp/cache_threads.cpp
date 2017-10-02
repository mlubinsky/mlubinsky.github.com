#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <thread>
#include <mutex>

using namespace std;

template <typename Key, typename Val, typename Tag>
class TCache {
  public:

      TCache() = delete; //because no default cache size

      TCache(size_t capacity) : _capacity(capacity) {
          _entries.reserve(capacity);
      };

      ~TCache() {  cout << "T Destructor"<< endl;  };

      /*---------------------------------------------------*/
      pair<Val, bool> get(Key key) {
        auto it = _entries.find(key);
        if (it != _entries.end()) {
            return make_pair(it->second, true);
        } else {
            return make_pair(Val(), false);
        }
      }

      /*---------------------------------------------------*/
      bool add(Key key, Val val, unordered_set<Tag> tags) {

           lock_guard<recursive_mutex> guard(mutex);
           if  (_entries.size() == _capacity)
             return false;   // better policy would be LRU cache

           auto result = _entries.insert({key,val});
           if (result.second) {
               for (auto t : tags){

                       auto it = _tag2key.find(t);
                       if (it != _tag2key.end()) {
                         _tag2key[t].insert(key);
                       } else {  // new tag
                         _tag2key.insert({t,(unordered_set<Key>){key}   });
                       }

                       _key2tag[key].insert(tags.begin(), tags.end());

               }
           }
           return result.second;
      }

    /*---------------------------------------------------*/
     bool removeByKey(Key key) {
        lock_guard<recursive_mutex> guard(mutex);

        auto it = _key2tag.find(key);
        if (it != _key2tag.end()) {

             for (auto tag: it->second){
                  _tag2key[tag].erase(key);
             }
        }

        _key2tag.erase(key);
        _entries.erase(key);

        return true;
     }

     /*---------------------------------------------------*/
      bool removeByTag(Tag tag) {
          lock_guard<recursive_mutex> guard(mutex);

          auto it = _tag2key.find(tag);
          vector<Key> keys;
          if (it == _tag2key.end())
            return false;

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
          cout << "----Display entry:  key=" << key ;
          auto it = _entries.find(key);
          if (it != _entries.end()) {
              cout <<  " Value="<< _entries[key] <<endl ;
           } else {
              cout << "No entry for Key="<< key << endl;
           }


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
              cout << "======Display all  cache size="  << size() << endl;
              for (pair<Key, Val> e: _entries){
                display(e.first);
              }
      }

      /*---------------------------------------------------*/
      void display_tags() {
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

   private:
      size_t _capacity;
      unordered_map<Key, Val> _entries;
      unordered_map<Tag, unordered_set<Key> > _tag2key;
      unordered_map<Key, unordered_set<Tag> > _key2tag;
      recursive_mutex mutex;
};

// Next function to be called from thread
void func1(TCache<int,int, int> &cache)
{
     cout << "Entering thread 1" << endl;

     bool result;
     unordered_set<int> tags;
     for (int key=1; key < 9; ++key) {
        tags.clear();
        tags.insert(key*2);
        tags.insert(key*3);
        result = cache.add(key, 10*key, tags);
     }

     this_thread::sleep_for(chrono::seconds(1));

     for (int key=1; key < 9; ++key) {
        pair<int,bool> v = cache.get(key);
        if (v.second)
             cout << " found ";
        else
             cout << " not found ";
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
        if (v.second)
             cout << " found ";
        else
             cout << " not found ";
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

    TCache<int,int, int> cache(5);   //create cache with capacity=5;  using integer keys, values and tags

    unordered_set<int> tags1({2,3,4,5});
    cache.add(1,10, tags1);

    unordered_set<int> tags2({4,5,6,7});
    cache.add(2,20, tags2);

    cache.display_all();
    cache.display_tags();

    cache.removeByTag(7);
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
    TCache<int,int,int> cache(5);  //using integer keys, values and tags, cache capacity=5
    thread firstThread(func1, ref(cache));
    thread secondThread(func1, ref(cache));
    firstThread.join();
    secondThread.join();
    return 0;
}