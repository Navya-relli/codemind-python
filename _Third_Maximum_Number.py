n=int(input())
z=list(map(int,input().split()))
a=set(z)
if len(a)<3:
    print(max(a))
else:
    a.remove(max(a))
    a.remove(max(a))
    print(max(a))