a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    s=0
    for j in range(i,b+1):
        s+=j
        if s%2!=0:
            c+=1
print(c)