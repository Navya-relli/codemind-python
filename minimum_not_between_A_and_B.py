n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=[]
for i in range(b,c+1):
    s.append(i)
d=[]
for j in a:
    if j not in s:
        d.append(j)
if len(d)>0:
    print(min(d))
else:
    print('-1')