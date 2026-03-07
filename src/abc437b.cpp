#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
int main(){
  int h,w,n;cin>>h>>w>>n;
  vector<vector<int>>a(h,vector<int>(w));
  rep(i,h)rep(j,w)cin>>a[i][j];
  vector<int>b(n);rep(i,n)cin>>b[i];
  int ans=0;
  rep(i,h){
    int cnt=0;
    rep(j,n)cnt+=count(a[i].begin(),a[i].end(),b[j]);
    ans=max(ans,cnt);
  }
  cout<<ans<<'\n';
}
