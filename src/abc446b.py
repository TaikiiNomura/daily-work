import sys
data = sys.stdin.read().split()
ptr = 0
n = int(data[ptr]); ptr += 1
m = int(data[ptr]); ptr += 1
chosed = [0 for _ in range(110)]
for _ in range(n):
  l = int(data[ptr]); ptr += 1
  x = list(map(int, data[ptr:ptr+l])); ptr += l
  ans = -1
  for i in range(l):
    if chosed[x[i]] == 0:
      ans = x[i]
      chosed[x[i]] += 1
      break
  if ans != -1:
    print(ans)
  else:
    print(0)
