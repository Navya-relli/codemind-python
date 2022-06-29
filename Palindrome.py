def rev(n):
    su=0
    while n>0:
        r=n%10
        su=(su*10)+r
        n=n//10
    return su
a=int(input())
if(a==rev(a)):
    print("True")
else:
    print("False")