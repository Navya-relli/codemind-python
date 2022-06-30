def count(a):
    if(a<=0):
        return 0
    elif(a==1):
        return 1
    elif(a==2):
        return 2
    elif(a==3):
        return 4
    return count(a-1)+count(a-2)+count(a-3)
a=int(input())

print(count(a))