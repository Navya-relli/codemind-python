a=int(input())
val=0
for i in range(a):
    t=input()
    if t=='++X':
        val+=1
    if t=='X++':
        val+=1
    if t=='--X':
        val-=1
    if t=='X--':
        val-=1
print(val)