h,w,q=map(int,input().split())
for _ in range(q):
    a,b=map(int,input().split())
    if a==1:
        print(b*w)
        h-=b
    else:
        print(b*h)
        w-=b
