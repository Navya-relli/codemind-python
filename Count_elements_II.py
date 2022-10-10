a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
p1=set(l)
p2=set(m)
p1=list(p1)
p2=list(p2)
for i in range(len(p1)):
    if p1[i] not in p2:
        c=c+1
for i in range(len(p2)):
    if p2[i] not in p1:
        c=c+1
print(c)