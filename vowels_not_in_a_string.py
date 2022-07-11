n=input()
k='aeiou'
p=[]
c=0
for i in n:
    if i in k and i  not in p:
        p.append(i)
for i in k:
    if i not in p:
        c=c+1
        print(i,end=" ")
if c==0:
    print(0)