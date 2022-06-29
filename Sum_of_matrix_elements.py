a=int(input())
b=int(input())
su=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in arr:
        su+=j
print(su)