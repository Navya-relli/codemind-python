n=int(input())
a=list(map(int,input().split()))
for i in a:
    if str(i).startswith('-'):
        print(len(str(i))-1,end=' ')
        continue
    print(len(str(i)),end=' ')