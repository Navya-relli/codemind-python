n=int(input())
a=list(map(int,input().split()))
s=0
p=0
for i in range(len(a)):
    if a[i]%2==0:
        s+=a[i]
for i in range(len(a)):
    if a[i]%2!=0:
        p+=a[i]
print(abs(s-p))
    