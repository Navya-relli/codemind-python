a=int(input())
for i in range (a):
    c=0
    if(i*(i+1)==a):
        c=1
        break
if(c==1):
    print("YES")
else:
    print("NO")   