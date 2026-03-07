#include<iostream>
#include<vector>
using namespace std;
int main()
{
  int n,m,ans=0;cin>>n>>m;
  vector<int>c(m);for(int&x:c)cin>>x;
  for(;n--;)
  {
    int a,b;cin>>a>>b;a--;
    if(c[a]>=b)
    {
      c[a]-=b;
      ans+=b;
    }
    else
    {
      ans+=c[a];
      c[a]=0;
    }
  }
  cout<<ans;
}
