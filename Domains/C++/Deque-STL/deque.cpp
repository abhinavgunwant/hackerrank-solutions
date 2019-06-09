#include <algorithm>
#include <iostream>
#include <deque>

using namespace std;

void printKMax(int arr[], int n, int k){
    deque<int> d;
    deque<int>::iterator itr;

    for(int i=0; i<n-k; ++i){
        for(int j=i; j<i+k-1; ++j){
            d.push_back(arr[j]);
        }
        itr = d.end();
        sort(d.begin(), itr);
        cout<<d[d.size()-1]<<"\n";
        d.pop_front();
    }
}
int main(){

   int t;
   cin >> t;
   while(t>0) {
      int n,k;
       cin >> n >> k;
       int i;
       int arr[n];
       for(i=0;i<n;i++)
            cin >> arr[i];
       printKMax(arr, n, k);
       t--;
     }
     return 0;
}
