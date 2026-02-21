print("Of",end="")
s = input()
for i in range(len(s)):
  if i == 0:
    print(s[i].lower(),end="")
  else:
    print(s[i],end="")
