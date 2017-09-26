#include <vector>
#include <thread>
#include <mutex>

#include <iostream>
using namespace std;

struct Counter {
    mutex m;
    int value;
    Counter() : value(0){}
    void increment(){
       m.lock();
       ++value;
       m.unlock();
   }
};


int main(){
    Counter counter;

    vector<thread> threads;
    for(int i = 0; i < 5; ++i){
        threads.push_back(thread([&counter](){
            for(int i = 0; i < 100; ++i){
                counter.increment();
            }
        }));
    }

    for(auto& thread : threads){
        thread.join();
    }

    cout << counter.value << endl;

    return 0;
}