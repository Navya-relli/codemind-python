n=list(input())
a=list(map(int,input().split()))
k=set(a)
d=list(k)
s=0
for i in d:
    if i%2==0:
        s=s+i
print(s)