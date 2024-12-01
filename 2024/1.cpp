#include <iostream>
#include <vector>
#include <stdlib.h> 
using namespace std;

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

    for(int i=0; i<n; i++){
        for(int ii=0; ii<n-i-1; ii++){
            if(left[ii]>left[ii+1]){
                int temp = left[ii];
                left[ii] = left[ii+1];
                left[ii+1] = temp;
            }
            if(right[ii]>right[ii+1]){
                int temp = right[ii];
                right[ii] = right[ii+1];
                right[ii+1] = temp;
            }
        }
    }

    int totalDiff = 0;

    for(int i=0; i<n; i++){
        totalDiff+=abs(left[i]-right[i]);
    }

    cout << totalDiff;

    return 0;
}