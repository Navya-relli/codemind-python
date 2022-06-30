a=input()
vow="aeiouAEIOU"
arr=[]
for i in a:
    if i in vow:
        arr.append(i)
i=len(arr)-1
s=""
for j in a:
    if j in vow:
        s+=arr[i]
        i-=1
    else:
        s+=j
print(s)