n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1):
    if a[i]<a[i+1]:
        c=c+1
if c+1==n:
    print('yes')
else:
    print('no')