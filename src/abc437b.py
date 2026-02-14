import sys
data = list(map(int, sys.stdin.read().split()))
ptr = 0

h = data[ptr]; ptr += 1
w = data[ptr]; ptr += 1
n = data[ptr]; ptr += 1
a = []
for i in range(h):
  a.append(data[ptr:ptr + w])
  ptr += w
b = data[ptr:ptr + n]

# print(a)
# print(b)
ans = 0
for row in a:
  cnt = 0
  for x in row:
    cnt += b.count(x)
  ans = max(cnt, ans)
print(ans)
