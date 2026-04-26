n=int(input())
l=list()
for i in range(n):
  q=input()
  if q=="2":
    print(l.pop(0))
  else:
    _,x=q.split()
    l.append(x)
