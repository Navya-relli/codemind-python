n=int(input())
l=list(map(int,input().split()))
l=set(l)
s=0
for i in l:
    if i%2==0:
        s+=1
print(s)