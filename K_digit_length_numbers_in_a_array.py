a,b=map(int,input().split())
n=list(map(int,input().split()))
c=0
for i in n:
    l=len(str(abs(i)))
    if b==l:
        c=c+1
print(c)