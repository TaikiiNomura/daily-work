def check(s,t):
  cnt=0
  for i in range(n):
    for j in range(n):
      if s[i][j]!=t[i][j]:
        cnt+=1
  return cnt

def rotate(l):
  L=[["."]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      L[i][j]=l[n-1-j][i]
  return L

n=int(input())
s=[input() for _ in range(n)]
t=[input() for _ in range(n)]
cnt=100000
for i in range(4):
  cnt=min(check(s,t)+i,cnt)
  s=rotate(s)
print(cnt)
