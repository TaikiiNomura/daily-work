#include<iostream>
using namespace std;
int main(){
  int n,a[110],k,cnt=0;
  cin>>n;
  for(int i=0;i<n;i++)cin>>a[i];
  cin>>k;
  for(int x:a)if(k<=x)cnt++;
  cout<<cnt;
}
