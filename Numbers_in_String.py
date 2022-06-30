a=input()
su=0
for i in a:
    if i.isdigit():
        su+=ord(i)-48
print(su)