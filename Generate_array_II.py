n=int(input())
arr=list(map(int,input().split()))
for i in range(1,n,2):
    for j in range(arr[i]):
        print(arr[i-1],end=" ")