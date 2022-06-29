a,b=map(int,input().split())
arr=[]
for i in range(a):
    arr1=list(map(int,input().split()))
    arr.append(arr1)
for i in range(b):
    m=0
    for j in range(a):
        if m<arr[j][i]:
            m=arr[j][i]
    print(m)