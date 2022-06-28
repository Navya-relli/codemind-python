a=list(map(int,input().split()))
b=list(map(int,input().split()))
alli=0
bob=0
for i in range(3):
    if a[i]>b[i]:
        alli+=1
    elif a[i]<b[i]:
        bob+=1
print(alli,bob)