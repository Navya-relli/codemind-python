n=int(input())
k=n
for i in range(1,2*n):
    k=n
    if(i<=n):
        for j in range(1,2*n):
            print(k,end=" ")
            if(i>j):
                k-=1
            if(i+j>=2*n):
                k+=1
    if(i>n):
        for j in range(1,2*n):
            print(k,end=" ")
            if(i+j<2*n):
                k-=1
            if(j>=i):
                k+=1
    print()            