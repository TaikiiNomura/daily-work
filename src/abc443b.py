import sys
input = sys.stdin.readline()

n, k = map(int, input.split())
# print(n, k)
sum = 0
ans = 0
while(sum < k):
    sum += n
    n += 1
    ans += 1
print(ans - 1)
