a=str(input())
b=a.split()
c=[]
d=[]
for i in range(len(b)):
    c.append(b[i])
for j in range(len(c)):
    m=c[j][::-1]
    d.append(m)
print(*d)