a=int(input())
arr=list(map(int,input().split()))
ma=-100
for i in range(a):
    su=0
    for j in range(i,a):
        su+=arr[j]
        if(ma<su):
            ma=su
print(ma)