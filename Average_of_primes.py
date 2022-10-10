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
s=0
c=0
k=list(map(int,input().split()))
for i in range(n):
    if prime(k[i]):
        s=s+k[i]
        c=c+1
ave=s/c
print(format(ave,".2f"))