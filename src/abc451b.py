import sys
data=sys.stdin.read().split()
it=iter(data)

n=int(next(it))
m=int(next(it))
A=[0]*(m+1)
B=[0]*(m+1)
for _ in range(n):
  a=int(next(it))
  b=int(next(it))
  A[a]+=1
  B[b]+=1
for i in range(1,m+1):
  print(B[i]-A[i])
