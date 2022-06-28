def perfect(n):
    if n==1:
        return 1
    for i in range(n):
        if i*i==n:
            return n
    return 0
z=int(input())
s=0
a=list(map(int,input().split()))
for i in range(z):
    b=perfect(a[i])
    s+=b
print(s)