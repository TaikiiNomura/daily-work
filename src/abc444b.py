import sys
it = sys.stdin.readline().split()

n, k = map(int, it)
ans = 0
for i in range(1, n+1):
  num = i
  sum = 0
  while(num > 0):
    sum += (num % 10)
    num //= 10
  # print(sum)
  if sum == k:
    ans += 1
print(ans)
