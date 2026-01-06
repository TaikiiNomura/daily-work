def happy(s):
    num=0
    for i in range(len(s)):
        num+=int(s[i])**2
    return str(num)

s=input()
cnt=0
while cnt<300:
    if s=="1":
        print("Yes")
        exit()
    s=happy(s)
    cnt+=1

print("No")