#include <iostream>
#include <vector>

using namespace std;

int ac = 0; //auxiliary carry
std::vector<std::vector<int> > v;
std::vector<int>::iterator it;

std::vector<int> sq(std::vector<int> a){
    int temp;
    std::vector<int>::iterator it = a.end(), loopend = a.begin();

    --it;
    --loopend;

    while(it != loopend){
        temp = *it;
        temp *= temp+ac;
        ac = 0;

        if(temp >= 10){
            ac = (int)temp/10;
            temp %= 10;
        }

        a.insert(a.begin(), temp);
        --it;

        cout<<"\n\t--"<<temp;
    }

    if(ac){
        a.insert(a.begin(), ac);
    }

    return a;
}

unsigned long long int f(int a, int b, int n){
    if(n == 0){
        return a;
    }

    if(n == 1){
        return b;
    }
    unsigned long long int temp = f(a, b, n-1);
    cout<<"\n\tn="<<n<<" "<<temp;
    return temp*temp + f(a, b, n-2);
}

int main(){
    int a, b, n;
    std::vector<int> num, ans;
    num.push_back(2);
    num.push_back(5);
    ans = sq(num);
    for(std::vector<int>::iterator itr = ans.begin(); itr != ans.end(); ++itr){
        cout<<*itr;
    }
    // cin>>a>>b>>n;

    // cout<<f(a, b, n);
    return 0;
}
