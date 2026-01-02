#include<iostream>
#include<string>
using namespace std;
#define rep(i,N) for(int i=0;i<(N);i++)
#define Yes {cout<<"Yes\n";return 0;}
#define No {cout<<"No\n";return 0;}
//
int N;
string T,S;
int main()
{
    cin>>N>>T>>S;
    rep(i,N)if(T[i]==S[i]&&'o'==T[i])Yes;
    No;
}