a=input()
zo=0
co=0
for i in a:
    if(i=='z'):
        zo+=1
    elif(i=='o'):
        co+=1
if(zo*2==co):
    print("Yes")
else:
    print("No")