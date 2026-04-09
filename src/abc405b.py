n,m=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
while(True):
  s=set(a)
  # print(s)
  if len(s)<m:
    break
  else:
    a.pop()
    cnt+=1
print(cnt)
