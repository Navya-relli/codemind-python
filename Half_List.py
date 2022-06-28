z=int(input())
a=list(map(int,input().split()))
b=z//2
for i in range(z-1,b-1,-1):
    print(a[i],end=' ')
for i in range(0,b,1):
    print(a[i],end=' ')