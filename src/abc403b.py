t=input()
u=input()
for i in range(len(t)-len(u)+1):
  t_=t[i:i+len(u)]
  isok=1
  for x,y in zip(t_,u):
    if x=='?':
      continue
    if x!=y:
      isok=0
  # print(t_,u,isok)
  if isok:
    print("Yes")
    exit()
print("No")
