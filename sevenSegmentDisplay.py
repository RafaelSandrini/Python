qty = [6,2,5,5,4,5,6,3,7,6]

T = int(input())
list=[]

for i in range(T):
    length = input()
    total = 0
    for j in length:
        x = int(j)
        total = total + int(qty[x])
    if total%2 != 0:
        number = (total-3)//2
        finalnumber = "7" + "1"*number
    else:
        number = total//2
        finalnumber = "1"*number
    list.append(finalnumber)

for a in range(0,len(list)):
	print (list[a])
