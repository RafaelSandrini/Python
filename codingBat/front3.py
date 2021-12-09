# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

def front3(str):
    length = len(str)
    if length <=3:
        front = str
    else:
        front = str[:3]
    return (3*front)

print (front3("rafael"))
print (front3("Java"))
print (front3("chocolate"))
print (front3("ab"))