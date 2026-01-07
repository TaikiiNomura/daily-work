#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
#define rep(i,N) for(int i=0;i<N;i++)
#define rng(x) x.begin(), x.end()
#define printv(v) rep(i,v.size())cout<<v[i]<<(i==v.size()-1?'\n':' ');
#define Yes {cout<<"Yes\n";return 0;}
#define No {cout<<"No\n";return 0;}
int main()
{
    int D,F; cin>>D>>F;
    cout<<7-(D-F)%7<<endl;
    return 0;
}
