a,b=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
p=[]
for i in arr1:
    if i in arr2 and i not in p:
        p.append(i)
print(*p)