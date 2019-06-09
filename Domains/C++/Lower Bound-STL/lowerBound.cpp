#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main() {
    int n, x, q, y, len;
    vector<int> vec;
    vector<int>::iterator beg, end, itr;
    // int vec[100000], *beg, *end;

    cin>>n;

    for(int i=0; i<n; ++i){
        cin>>x;
        vec.push_back(x);
    }

    // len = n;
    // beg = vec;
    // end = vec + n;

    len = vec.size();
    beg = vec.begin();
    end = vec.end();

    cin>>q;

    for(int i=0; i<q; ++i){
        cin>>y;

        if(find(beg, end, y) != end){
            cout<<"Yes "<<lower_bound(beg, end, y) - beg+1<<"\n";
        }else{
            cout<<"No "<<lower_bound(beg, end, y) - beg+1<<"\n";
        }
    }

    return 0;
}
