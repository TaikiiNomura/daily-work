n=int(input())
s=[input() for _ in range(n)]
S=set()
for i in range(n):
  for j in range(n):
    if i==j:continue
    str=s[i]+s[j]
    S.add(str)
print(len(S))
