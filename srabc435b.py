import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
  for j in range(n):
    if i > j:
      continue
    num = sum(a[i:j+1])
    isok = True
    for x in range(i, j+1):
      # 一つでも約数の場合ダメ
      if num % a[x] == 0:
        isok = False
        break
    if isok:
      ans += 1
      # print(i+1, j+1)

print(ans)
