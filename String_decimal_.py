a=int(input())
for i in range (a):
    l=input()
    f=0
    for j in l:
        if j.isdigit():
            f=1
        else:
            f=0
            break
    if(f==1):
        print("True")
    else:
       print("False")