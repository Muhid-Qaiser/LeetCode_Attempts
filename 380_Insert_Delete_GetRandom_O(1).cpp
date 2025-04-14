class RandomizedSet {
    unordered_set<int> mySet;
public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        if (mySet.find(val) == mySet.end())
        {
            mySet.insert(val);
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        if (mySet.find(val) != mySet.end())
        {
            mySet.erase(val);
            return true;
        }
        return false;
    }
    
    int getRandom() {
        int randomValue = rand() % mySet.size() + 1;
        vector<int> myVec(mySet.begin(), mySet.end()); 
        return myVec[randomValue-1];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */