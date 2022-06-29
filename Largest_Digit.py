a=int(input())
maxd=0
while a>0:
    rem=a%10
    if rem>maxd:
        maxd=rem
    a//=10
print(maxd)