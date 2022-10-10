def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
b=list(map(int,input().split()))
c=0
for i in range(n):
    if prime(b[i]):
        c=c+1
print(c)