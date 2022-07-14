n=int(input())
m=0
c=0
a=list(map(int,input().split()))
for i in a:
    l=len(str(i))
    if m<l:
        m=l
for i in a:
    if len(str(i))==m:
        print(i,end=' ')