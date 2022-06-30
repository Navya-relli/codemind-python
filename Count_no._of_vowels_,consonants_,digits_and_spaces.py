a=input()
vo=["a","e","i","o","u","A","E","I","O","U"]
vou=con=di=sp=0
for i in a:
    if i.isdigit():
        di+=1
    elif i==" ":
        sp+=1
    else:
        if(i in vo):
            vou+=1
        else:
            con+=1
            
print("Vowels:",vou)
print("Consonants:",con)
print("Digits:",di)
print("White spaces:",sp)