n=input()
k='aeiou'
c=0
s=n.split()
for i in s:
    for j in i:
        if j in k:
            c=c+1
    print(c,end=" ")
    c=0