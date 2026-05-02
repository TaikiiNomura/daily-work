inf=1e9;num=0
n,m=map(int,input().split())
for i in range(m+1):
  num+=n**i
  if num>inf:
    print("inf")
    exit()
print(num)
