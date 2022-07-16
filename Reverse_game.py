def palindrome(n):
    p=0
    while n:
        r=n%10
        n=n//10
        p=p*10+r
    return p
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    p=palindrome(i)
    print(p,end=' ')