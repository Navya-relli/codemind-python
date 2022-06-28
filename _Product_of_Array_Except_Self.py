n=int(input())
a=list(map(int,input().split()))
b=[]
p=1
for i in range(n):
    for j in range(n):
        if i!=j:
            p*=a[j]
        k=p
    b.append(k)
    p=1
print(*b)