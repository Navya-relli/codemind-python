n=input()
s=n.split()
max=0
c=0
for i in s:
    c=len(i)
    if max<c:
        max=c
print(max)