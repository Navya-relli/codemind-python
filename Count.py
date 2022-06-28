z=int(input())
c=0
d=0
a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        c+=1
    else:
        d+=1
print(c,d)