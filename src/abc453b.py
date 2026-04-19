n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
past=0
for i,aa in enumerate(a):
  if i==0 or abs(aa-past)>=x:
    ans.append((i,aa))
    past=aa
for t,a in ans:
  print(t,a)
