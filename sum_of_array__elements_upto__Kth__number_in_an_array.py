n=int(input())
a=list(map(int,input().split()))
b=int(input())
s=0
for i in range(n):
    if a[i]>b:
        break
    else:
        s=s+a[i]
print(s)