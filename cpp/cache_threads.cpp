#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <thread>
#include <mutex>
//#include <shared_mutex>
using namespace std;


template <typename Key, typename Val>
class TCache {
  public:

      TCache() = delete; //because no default cache size

      TCache(size_t capacity) : _capacity(capacity) {
          _entries.reserve(capacity);
      };

      ~TCache() {  cout << "T Destructor"<< endl;  };

      /*---------------------------------------------------*/
      std::pair<Val, bool> get(Key key) {
        auto it = _entries.find(key);
        if (it != _entries.end()) {
            return std::make_pair(it->second, true);
        } else {
            return std::make_pair(Val(), false);
        }
      }

      /*---------------------------------------------------*/
      bool add(Key key, Val val, unordered_set<int> tags) {
          //Exclusive lock - single writer only
          //std::unique_lock<std::shared_timed_mutex> lock(mutex_);
           std::lock_guard<std::mutex> guard(mutex);
           if  (_entries.size() == _capacity) //better policy - LRU cache
             return false;
           auto result = _entries.insert({key,val});
           if (result.second) {
               for (auto t : tags){
                       auto it = _tags.find(t);
                       if (it != _tags.end()) {  // tag exists
                         //cout <<" Add tags - tag exists" << endl;
                         _tags[t].insert(key);
                       } else {  // new tag
                          //cout <<" Add tags - new tag " << endl;
                         _tags.insert({t,(unordered_set<int>){key}   });
                       }
               }
           }
           return result.second;
      }

     /*---------------------------------------------------*/
      bool removeByTag(int tag) {
          std::lock_guard<std::mutex> guard(mutex);
          cout << "======removeByTag() tag=" << tag << endl;
          auto it = _tags.find(tag);
          if (it != _tags.end()) {

                for (auto key: it->second){
                   cout << " Key to be deleted " << key;
                   _entries.erase(key);
                   _tags[tag].erase(key);
                }

          }
          cout << endl;
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
      }

      void display_all() {
              cout << "======Display all  cache size="  << size() << endl;
              for (std::pair<Key, Val> e: _entries){
                display(e.first);
              }
      }

      /*---------------------------------------------------*/
      void display_tags() {
             cout << "======Display tags===" << endl;
             for (auto t: _tags){
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
    bool removeByKey(Key);  // not implemented because no effective way to find and remove from _tags by value

   private:
      size_t _capacity;
      unordered_map<Key, Val> _entries;
      unordered_map<int, unordered_set<int> > _tags;
      std::mutex mutex;
      //std::recursive_mutex mutex;
      //mutable std::shared_timed_mutex mutex_;
};

// Next function to be called from thread
void func1(TCache<int,int> &cache)
{
     std::cout << "Entering thread 1" << std::endl;

     bool result;
     unordered_set<int> tags;
     for (int key=1; key < 9; ++key) {
        tags.clear();
        tags.insert(key*2);
        tags.insert(key*3);
        result = cache.add(key, 10*key, tags);
        //cout << "Key=" << key << "  Insert result=" << result << endl;
     }

     std::this_thread::sleep_for(std::chrono::seconds(1));

     for (int key=1; key < 9; ++key) {
        std::pair<int,bool> v = cache.get(key);
     }

     std::this_thread::sleep_for(std::chrono::seconds(1));

     for (int tag=1; tag < 9; ++tag) {
        cache.removeByTag(tag);
     }
}

// Next function to be called from thread
void func2(TCache<int,int> &cache)
{
     std::cout << "Entering thread 2" << std::endl;
     bool result;

     for (int tag=1; tag < 9; ++tag) {
        cache.removeByTag(tag);
     }

     std::this_thread::sleep_for(std::chrono::seconds(1));

     for (int key=1; key < 9; ++key) {
        std::pair<int,bool> v = cache.get(key);
     }

     std::this_thread::sleep_for(std::chrono::seconds(1));

     unordered_set<int> tags;
     for (int key=1; key < 9; ++key) {
        tags.clear();
        tags.insert(key*2);
        tags.insert(key*3);
        result = cache.add(key, 10*key, tags);
        //cout << "Key=" << key << "  Insert result=" << result << endl;
     }
}


void test_single_thread () {

    TCache<int,int> cache(5);   //create cache with capacity=5

    std::unordered_set<int> tags1({2,3,4,5});
    cache.add(1,10, tags1);

    std::unordered_set<int> tags2({4,5,6,7});
    cache.add(2,20, tags2);

    cache.display_all();
    cache.display_tags();

    cache.removeByTag(7);
    std::pair<int,bool> v = cache.get(1);
    if (v.second)
       cout << "Found entry for key = 1 value=" << v.first << endl;
     else
        cout << "Not found entry for key = 1 "<< endl;

    cache.display_all();
    cache.display_tags();

}

int main ( int argc,  char** argv) {
    test_single_thread();

    // test several threads
    TCache<int,int> cache(5);
    std::thread firstThread(func1, ref(cache));
    std::thread secondThread(func1, ref(cache));
    firstThread.join();
    secondThread.join();
    return 0;
}