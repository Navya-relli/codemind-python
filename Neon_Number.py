a=int(input())
asq=a**2
su=0
temp=asq
while temp>0:
    rem=temp%10
    su+=rem
    temp//=10
if su==a:
    print("Neon Number")
else:
    print("Not Neon Number")