z=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b and a.count(i)>=1:
        b.append(i)
print(*b)