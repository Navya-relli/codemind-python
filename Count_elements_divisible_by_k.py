n,k=map(int,input().split())
c=0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%k==0:
        c=c+1
print(c)