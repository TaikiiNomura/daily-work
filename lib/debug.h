
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#include<bits/stdc++.h>
using namespace std;

using ll=long long;
using ull=unsigned long long;
using ld=long double;
using pii=pair<int,int>;
using pll=pair<ll,ll>;
template<class T>using vc=vector<T>;
template<class T>using vvc=vc<vc<T>>;

#define rep(i,n) for(int i=0;i<(n);i++)
#define rrep(i,n) for(int i=(n)-1;i>=0;i--)
#define reps(i,a,b) for(int i=(a);i<(b);i++)
#define all(x) (x).begin(),(x).end()
#define pb push_back

template<class T>bool chmax(T&a,const T&b){
  if(a<b){
    a=b;
    return true;
  }
  return false;
}
template<class T>bool chmin(T&a,const T&b){
  if(a>b){
    a=b;
    return true;
  }
  return false;
}

int main(){
  ios::sync_with_stdio(false);cin.tie(nullptr);

  int n;cin>>n;
  vc<int>a(n);
  rep(i,n)cin>>a[i];

}
