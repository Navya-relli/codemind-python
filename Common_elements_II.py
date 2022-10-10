a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
d=[]
for i in l1:
    if i not in l2:
        print(i,end=" ")
for i in l2:
    if i not in l1:
        print(i,end=" ")