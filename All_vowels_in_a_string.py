n=input()
k='aeiou'
p=[]
c=0
for i in n:
    if i in k and i not in p:
        p.append(i)
        
if len(p)==5:
    print("True")
else:
    print("False")