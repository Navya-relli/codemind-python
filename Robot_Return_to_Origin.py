a=input()
up=down=left=right=0
for i in a:
    if i=='U':
        up+=1
    elif i=='D':
        down+=1
    elif i=='L':
        left+=1
    elif i=='R':
        right+=1
if left==right and up==down:
    print("True")
else:
    print("False")