# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
    length = len(str)
    if length <= 1:
        result = str
    else:
        middle = str[1:length-1]
        result = str[length-1]+middle+str[0]
    return result

print (front_back("rafael"))
print (front_back("code"))
print (front_back("a"))
print (front_back("ab"))
