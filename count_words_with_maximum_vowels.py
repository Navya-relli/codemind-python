x=list(map(str,input().split()))
n=[]
s=0
l=['a','e','i','o','u']
for i in x:
    for j in i:
        if j in l:
            s+=1
    n.append(s)
    s=0
m=max(n)
print(n.count(m))