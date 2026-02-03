#include<bits/stdc++.h>
using namespace std;
int main()
{
  // int a = 'a' - '0';
  // cout << a << endl;
  // int z = 'z' - '0';
  // cout << z << endl;
  // 49
  // 74
  string s;
  cin >> s;
  int n = s.size();
  
  for(int i = 49; i <= 74; i++)
  {
    bool isok = true;
    for(int j = 0; j < n; j++)
    {
      if(s[j] - '0' == i) 
      {
        isok = false;
        break;
      }
    }
    if(isok)
    {
      cout << char(i + '0');
      return 0;
    }
  }
}
