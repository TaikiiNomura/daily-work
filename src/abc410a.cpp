#include<iostream>
using namespace std;
#define rep(i,N) for(int i=0;i<(N);i++)
int N,A[110],K,cnt=0;
int main()
{
    cin>>N;
    rep(i,N)cin>>A[i];
    cin>>K;

    rep(i,N)if(K<=A[i])cnt++;
    cout<<cnt<<'\n';
    return 0;
}