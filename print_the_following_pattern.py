n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n or j==n-1:
            continue
        else:
            print(j,end="")
    for k in range(1,n-2):
        print(k,end="")
    print()