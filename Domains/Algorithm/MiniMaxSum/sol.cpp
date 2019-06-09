#include <bits/stdc++.h>

using namespace std;

bool des(int a, int b){
    return a > b;
}

vector<long long> solve(vector<long long> a){
    int len = a.size();
    long long sum = 0;
    vector<long long> res;
    res.push_back(-1);
    res.push_back(-1);
    vector<long long>::iterator min = res.begin();
    vector<long long>::iterator max = res.end()-1;

    sort(a.begin(), a.end());
    for(int i=0; i<4; ++i){
        sum += a[i];
    }

    *min = sum;
    sum = 0;
    sort(a.begin(), a.end(), des);

    for(int i=0; i<4; ++i){
        sum += a[i];
    }

    *max = sum;
    return res;
}


int main() {
    vector<long long> arr(5);
    vector<long long> result;
    for(int i = 0; i < 5; ++i){
       cin >> arr[i];
    }

    result = solve(arr);

    for(int i=0; i<result.size(); ++i){
        if(i > 0){
            cout<<' ';
        }
        cout<<result[i];
    }
    return 0;
}
