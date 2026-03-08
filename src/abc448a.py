n,x=map(int,input().split())
aa=list(map(int,input().split()))
for a in aa:
  if a<x:
    x=a
    print(1)
  else:
    print(0)
