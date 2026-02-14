#pragma GCC target("avx2")
#pragma GCC optimize(03)
#pragma GCC optimize("unroll-loops")

#include<bits/stdc++.h>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); i++)

int main() {
  ios::sync_with_stdio(false); cin.tie(nullptr);
  
  int h, w, n; cin >> h >> w >> n;
  vector<vector<int> > a(h, vector<int>(w));
  rep(i, h)rep(j, w)cin >> a[i][j];
  vector<int> b(n); rep(i, n)cin >> b[i];
  
  vector<int> ans;
  rep(i, h) {
    int cnt = 0;
    rep(j, n)cnt += count(a[i].begin(), a[i].end(), b[j]);
    // cout << cnt << endl;
    ans.push_back(cnt);
  }
  cout << *max_element(ans.begin(), ans.end());
}
