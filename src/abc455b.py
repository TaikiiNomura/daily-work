def check(hs,he,ws,we):
  for i in range(hs,he+1):
    for j in range(ws,we+1):
      if s[i][j]!=s[hs+he-i][ws+we-j]:
        return 0
  return 1
cnt=0
h,w=map(int,input().split())
s=[input() for _ in range(h)]
for hs in range(0,h):
  for he in range(hs,h):
    for ws in range(0,w):
      for we in range(ws,w):
        # print(hs,he,ws,we,check(hs,he,ws,we))
        cnt+=check(hs,he,ws,we)
print(cnt)
