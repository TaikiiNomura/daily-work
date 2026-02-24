import sys
input = sys.stdin.readline
n = int(input())
s = [input().strip() for _ in range(n)]
t = 0
for i in range(n):
  t = max(t, len(s[i]))
for i in range(n):
  cnt = (t - len(s[i])) // 2
  ans = ""
  ans += '.'*cnt
  ans += s[i]
  ans += '.'*cnt
  print(ans)
