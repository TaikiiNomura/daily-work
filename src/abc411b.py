n=int(input())
d=list(map(int,input().split()))
for i in range(n):
  for j in range(i+1,n):
    dist=0
    for k in range(i,j):
      dist+=d[k]
    print(dist,end='')
    if j==n-1:
      print()
    else:
      print(' ',end='')
