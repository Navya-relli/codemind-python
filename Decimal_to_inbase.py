a=int(input())
b=int(input())
arr=[]
while a>0:
    r=a%b
    arr.append(r)
    a=a//b
f=c=0
for i in range(len(arr)):
    c=0
    for j in range(i,len(arr)):
        if(arr[j]==0):
            c+=1
            if(f<c):
                f=c
        else:
            break
if(f==0):
    print(-1)
else:
    print(f)