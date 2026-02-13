import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

sort_t = sorted(t)

for j in range(n):
  if j == 3:
    break
  for i in range(n):
    if t[i] == sort_t[j]:
      print(i + 1)
      break
