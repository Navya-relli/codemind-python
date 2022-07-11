a=str(input())
b=a.split()
c=[]
e=[]
for i in range(len(b)):
    c.append(b[i])
for j in range(len(c)):
    if j%2==0:
        m=c[j][::-1]
        e.append(m)
    else:
        e.append(c[j])
print(*e)