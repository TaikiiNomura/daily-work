n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-2):
  if l[i]==l[i+1]==l[i+2]:
    print("Yes")
    exit()
print("No")
