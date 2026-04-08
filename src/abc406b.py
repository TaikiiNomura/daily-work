n,k=map(int,input().split())
a=list(map(int,input().split()))
num=1
for x in a:
  num*=x
  if len(str(num))>k:
    num=1
print(num)
