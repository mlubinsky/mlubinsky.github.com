class LRUCache {
public:
    LRUCache(int capacity) : _capacity(capacity) {}

    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;
        touch(it);
        return it->second.first;
    }

    void set(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end())
           touch(it);
        else {
			if (cache.size() == _capacity) {
				cache.erase(used.back());
				used.pop_back();
			}
            used.push_front(key);
        }
        cache[key] = { value, used.begin() };
    }

private:
    //typedef list<int> LI;
    typedef pair<int, list<int>::iterator> PII;
    typedef unordered_map<int, PII> HIPII;   // key -> (value,position in linked list)

    void touch(HIPII::iterator it) { // move to front of linked list
        int key = it->first;
        used.erase(it->second.second);  //erase from link list for given iterator
        used.push_front(key);             // add to beginning of list
        it->second.second = used.begin(); //points to beginning of linked list
    }

    HIPII cache;
    list<int>  used;
    int _capacity;
};
