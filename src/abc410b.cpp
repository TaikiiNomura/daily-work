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
    int N,Q; cin>>N>>Q;
    vector<int> B(N,0);
    
    rep(i,Q)
    {
        int X; cin>>X;
        if(X>=1)
        {
            B[X-1]++;
            cout<<X;
        }
        else
        {
            int min_val=*min_element(rng(B));
            rep(j,N)if(B[j]==min_val)
            {
                cout<<j+1;
                B[j]++;
                break;
            }
        }
        if(i==(Q-1))cout<<endl;
        else cout<<' ';
    }
    // printv(B);
}