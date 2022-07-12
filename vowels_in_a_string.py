n=input()
e=input()
p=0
for i in str(n):
    if i==e:
        print('True')
        print(p)
        break
    p=p+1
else:
    print('False')