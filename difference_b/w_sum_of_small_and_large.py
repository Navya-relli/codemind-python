a=str(input())
b=a.split()
c=[]
d=[]
s1=0
s2=0
for i in b:
    c.append(min(i))
for i in b:
    d.append(max(i))
for i in c:
    s2=s2+ord(i)
for i in d:
    s1=s1+ord(i)
print(s1-s2)