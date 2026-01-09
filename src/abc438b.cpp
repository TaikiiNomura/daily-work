#include<bits/stdc++.h>
using namespace std;
int n,m,a=1e9,i,j,r;string s,t;
int main(){
  cin>>n>>m>>s>>t;
  for(i=0;i<=n-m;i++){
      r=0;
      for(j=0;j<m;j++) r+=(s[i+j]-t[j]+10)%10;
      a=min(a,r);
  }    cout<<a;
}
