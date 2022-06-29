a=int(input())
b=c=d=r=rev=0
while a>0:
    b=a%10
    a//=10
    r=r*10+b
while r>0:
    c=r%10
    r//=10
    if d<1:
        if c==6:
            c=9
            d=1
    rev=rev*10+c
print(rev)