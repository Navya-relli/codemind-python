a=list(map(int,input().split()))
m=0
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            p=(a[i]-1)*(a[j]-1)
            if(p>m):
                m=p
print(m)   