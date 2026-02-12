import sys
input = sys.stdin.readline
n, k = map(int,input().split())
s = input()
t = input()
q = int(input())
for _ in range(q):
  w = input()
  is_aoki = True
  is_taka = True
  for c in w:
    if s.count(c) == 0:
      is_aoki = False
    if t.count(c) == 0:
      is_taka = False
  # print(is_aoki, is_taka)
  if is_aoki and not is_taka:
    print("Takahashi")
  elif not is_aoki and is_taka:
    print("Aoki")
  else:
    print("Unknown")
