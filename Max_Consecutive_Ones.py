n=int(input())
s=input()
c=0
c1=0
for i in s:
    if i=='1':
        c+=1
    if i=='0':
        if c>c1:
            c1=c
        c=0
if c1<c:
    c1=c
print(c1)