s1=str(input())
s2=str(input())
a=s1.lower()
b=s2.lower()
d=list(a)
e=list(b)
f=[]
g=[]
c='abcdefghijklmnopqrstuvwxyz'
for i in d:
    if i!='':
        if i not in e:
            f.append(i)
for i in e:
    if i!='':
        if i not in d:
            f.append(i)
for i in c:
    if i in f:
        g.append(i)
print(len(g))