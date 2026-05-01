cnt=0;state="logout"
n=int(input())
for _ in range(n):
  s=input()
  if s[0]=='l':
    state=s
  else:
    if s=="private" and state=="logout":
      cnt+=1
print(cnt)
