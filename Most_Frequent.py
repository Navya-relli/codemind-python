z=int(input())
a=list(map(int,input().split()))
m=0
for i in range(z):
    c=a.count(i)
    if c>m:
        m=c
        max=i
print(max)  