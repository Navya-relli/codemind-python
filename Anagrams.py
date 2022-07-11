n1=input()
n2=input()
n3=n1.lower()
n4=n2.lower()
c=0
for i in n3:
    if i in n4:
        c=c+1
if c==len(n3)==len(n4):
    print("True")
else:
    print("False")