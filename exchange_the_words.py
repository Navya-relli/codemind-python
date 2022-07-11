a=str(input())
b=a.split()
c=[]
e=[]
for i in range(len(b)):
    c.append(b[i])
print(*(c[::-1]))