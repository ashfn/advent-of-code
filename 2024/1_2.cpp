#include <iostream>
#include <vector>
#include <stdlib.h> 
#include <map>
using namespace std;


int getNum(map<int, int> cache, int x, vector<int> right){
    if (cache.count(x)){
        return cache[x];
    }else{
        int count = 0;
        for(int i=0; i<right.size(); i++){
            if(right[i]==x){
                count++;
            }
        }
        cache[x] = count;
        return count;
    }
}

int main(){
    int n;
    cin >> n;

    vector<int> left = {};
    vector<int> right = {};

    for(int i=0; i<n; i++){
        int l;
        int r;
        cin >> l;
        cin >> r;
        left.push_back(l);
        right.push_back(r);
    }

    map<int, int> cache = {};

    int totalScore = 0;

    for(int i=0; i<left.size(); i++){
        int num = left[i];
        totalScore+=(num*getNum(cache, num, right));
    }

    cout << totalScore;

    return 0;
}