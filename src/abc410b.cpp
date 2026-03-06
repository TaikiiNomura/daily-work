#include<iostream>
using namespace std;
int n,q,b[110];
int main()
{
  cin>>n>>q;
  for(int i=0;i<q;i++)
  {
    int x;cin>>x;
    if(x==0)
    {
      int cnt_min=10000;
      for(int j=0;j<n;j++)cnt_min=min(b[j],cnt_min);
      for(int j=0;j<n;j++)if(b[j]==cnt_min)
      {
        b[j]++;
        cout<<j+1;
        break;
      }
    }
    else
    {
      b[x-1]++;
      cout<<x;
    }
    cout<<(i==q-1?'\n':' ');
  }
}
