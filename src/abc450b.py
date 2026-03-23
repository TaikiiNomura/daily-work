n=int(input())
l=[list(map(int,input().split())) for _ in range(n-1)]
ans="No"
for a in range(n-2):
  for b in range(a+1,n-1):
    for c in range(b+1,n):
      if l[a][b-1-a]+l[b][c-1-b]<l[a][c-1-a]:
        ans="Yes"
print(ans)
