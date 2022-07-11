n,l=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    k=abs(arr[i])
    if len(str(k))==l:
        c=c+1
print(c)