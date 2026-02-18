import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
  isok = False
  
  idx = -1
  for j in range(i):
    if a[j] > a[i]:
      isok = True
      if idx < j:
        idx = j
  
  if isok:
    print(idx+1)
  else:
    print(-1)
