n=int(input())
s=input()
ans=""
is_o=True
for ss in s:
  if ss=='o' and is_o:
    pass
  else:
    ans+=ss
    is_o=False
print(ans)
