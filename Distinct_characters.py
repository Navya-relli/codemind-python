a=str(input())
b=a.lower()
c=list(b)
d=[]
f=[]
e='abcdefghijklmnopqrstuvwxyz'
for i in c:
    if i!='':
        if i not in d:
            d.append(i)
for i in e:
    if i in d:
        f.append(i)
g=''.join(f)
print(g)