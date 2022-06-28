def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
a=int(input())
b=int(input())
i=a
d=0
while i<=b:
    if(prime(i)):
        d=d+1
    i=i+1
print(d)