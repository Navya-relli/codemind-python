def reverse(s):
    if len(s)==1:
        return s
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return s1
a=input()
maxs=""
c=0
for i in range(len(a)):
    s=""
    for j in range(i,len(a)):
        s+=a[j]
        if s==reverse(s):
            if s in a:
                if(len(s)>c):
                    maxs=s
                    c=len(s)
print(maxs)