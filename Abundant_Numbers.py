a=int(input())
su=0
for i in range(1,a):
    if a%i==0:
        su+=i
if su>a:
    print("True")
else:
    print("False")