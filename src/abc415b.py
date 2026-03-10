s=input()
cnt=0
first=0
for i in range(len(s)):
  if s[i]=='#':
    cnt+=1
    if cnt==2:
      print(f'{first},{i+1}')
      cnt=0
      first=0
    else:
      first=i+1
