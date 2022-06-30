st=input()
n=int(input())
cont=0
d=0

for i in st:
    d+=1
    if i=='a':
        cont+=1
t=n//d
r=n%d
full=cont*t
for i in range(r):
    if(st[i]=='a'):
        full+=1
print(full)