s=input()
t=input()
ans="Yes"
for i in range(1,len(s)):
  if s[i].isupper():
    if s[i-1] not in t:
      ans="No"
      break
print(ans)
