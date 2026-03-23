n=int(input())
l=[list(map(int,input().split())) for _ in range(n-1)]
for a in range(n-2):
  for b in range(a+1,n-1):
    for c in range(b+1,n):
      abc=l[a][b-1-a]+l[b][c-1-b]
      ac=l[a][c-1-a]
      # print(a,b,c,abc,ac)
      if abc<ac:
        print("Yes")
        exit()
print("No")
