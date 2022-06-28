n=int(input())
s=0
b=[]
for i in range(n):
    a=int(input())
    b.append(a)
p=int(input())
for i in range(n):
    if b[i]<=p:
        s+=1
    else:
        s+=2
print(s)