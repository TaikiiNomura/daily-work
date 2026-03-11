n=int(input())
cnt=0
ans=""
for i in range(n):
  c,l=input().split()
  cnt+=int(l)
  if cnt>100:
    print("Too Long")
    exit()
  for _ in range(int(l)):
    ans+=c
print(ans)
