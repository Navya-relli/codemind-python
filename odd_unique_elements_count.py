n=list(input())
a=list(map(int,input().split()))
k=set(a)
d=list(k)
c=0
for i in d:
    if i%2!=0:
        c=c+1
print(c)