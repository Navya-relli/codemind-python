n=int(input())
a=list(map(int,input().split()))
for i in range(n-1,0+1,-1):
    if a[i]%2!=0:
        print(i)
        break