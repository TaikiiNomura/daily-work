n = int(input())
a = list(map(int, input().split()))
k = int(input())

cnt = 0
for d in a:
  if k <= d:
    cnt += 1

print(cnt)
