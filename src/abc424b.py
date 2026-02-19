import sys
from collections import defaultdict

input = sys.stdin.readline
dd = defaultdict(list)

n, m, k = map(int, input().split())
ansed = []
for _ in range(k):
  a, b = map(str, input().split())
  dd[a].append(b)

  for k, v in dd.items():
    if len(v) == m and ansed.count(k) == 0:
      print(k)
      ansed.append(k)
