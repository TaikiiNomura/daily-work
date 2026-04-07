x,y=map(int,input().split())
c=sum(i+j>=x or abs(i-j)>=y for j in range(1,7) for i in range(1,7))
print(c/36)
