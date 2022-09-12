s=input()
c=''
p=0
for i in s:
    if i not in c:
        c=c+i
        p=p+1
    else:
        print(False)
        break
if p==len(s):
    print(True)