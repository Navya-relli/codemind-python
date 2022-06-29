a=int(input())
r=0
while a>0:
    l=a%10
    r=(r*10)+l
    a=a//10
print(r)