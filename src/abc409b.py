n=int(input())
l=list(map(int,input().split()))
a=[0]*(n+1)
for i in range(n,-1,-1):
  cnt=0
  for x in l:
    if i<=x:
      cnt+=1
  a[i]=cnt
  if cnt>=i:
    print(i)
    exit()
