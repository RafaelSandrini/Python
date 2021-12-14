string = input()
newstring = ""
for i in string:
    if i.isupper():
        x = i.lower()
        newstring = newstring + x
    else:
        x = i.upper()
        newstring = newstring + x

print (newstring)