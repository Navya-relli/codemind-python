n,p=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%p==0:
        c=c+1
print(c)