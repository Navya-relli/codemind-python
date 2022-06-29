def none(n):
    su=0
    for i in range(1,n):
        if(n%i==0):
            su+=i
    return su
a=int(input())
if(none(a)==a):
    print("True")
else:
    print("False")