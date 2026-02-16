import sys
input = sys.stdin.readline

n = int(input().strip())
g = [[0 for _ in range(n)] for _ in range(n)]
r = 0
c = (n-1)//2
k = 1
g[r][c] = k
cnt = 0
while(cnt < n*n - 1):
  cnt += 1
  if g[(r - 1) % n][(c + 1) % n] == 0:
    r = (r - 1) % n
    c = (c + 1) % n
  else:
    r = (r + 1) % n
  k += 1
  g[r][c] = k
for i in range(n):
  print(*g[i])
