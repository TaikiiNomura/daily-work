import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for j in range(m):
    if b[j] in a:
        a.remove(b[j])
print(*a)
