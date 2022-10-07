n=int(input())
a=list(map(int,input().split()))
s=[]
if n%2!=0:
    for i in range(0,n//2+1):
        if a[i]!=a[n-1-i]:
            s.append(a[i])
            s.append(a[n-1-i])
        else:
            s.append(a[i])
            s.append(0)
else:
    for i in range(0,n//2):
        s.append(a[i])
        s.append(a[n-1-i])
print(*s)
                