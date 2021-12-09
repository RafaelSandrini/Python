word = input()
x = 0
y = 0
for i in range(len(word)):
    if word[i]=="z":
        x += 1
    if word[i]=="o":
        y += 1

if y == 2*x:
    print("Yes")
else:
    print ("No")

print ("test")
    

    
    