n=input()
s=n.split()
l=len(s)
k=s[l-1]
p=k.lower()
for i in p:
    if p.count(i)>=2:
        print(min(p))
        break
else:
    print(min(k))