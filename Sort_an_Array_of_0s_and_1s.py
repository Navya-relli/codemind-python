n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i<1:
        print(i,end=' ')
    else:
        c=c+1
for i in range(c):
    print('1',end=' ')