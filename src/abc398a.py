n=int(input())
s=""
for i in range(1,n+1):
  if n%2==0 and i==n//2:
    s+='='
  elif i==n//2+1:
    s+='='
  else:
    s+='-'
print(s)
