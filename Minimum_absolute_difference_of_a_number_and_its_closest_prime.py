def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
df=dl=l=f=0
for i in range(a,0,-1):
    if prime(i)==1:
        f=i
        df=a-i
        break
for i in range(a,10000):
    if prime(i)==1:
        l=i
        dl=i-a
        break
if df==dl:
    print(dl)
elif df>dl:
    print(dl)
elif df<dl:
    print(df)