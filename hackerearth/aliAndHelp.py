tag = input()
def checktag(tag):
    vowel = ["A","E","I","O","U","Y"]
    answer = ""
    initial = tag[:2]
    middle = tag[3:6]
    end = tag[7:9]
    if (int(initial[0]) + int(initial[1]))%2 != 0:
        answer = "invalid"
        return answer
    elif (int(middle[0]) + int(middle[1]))%2 != 0:
        answer = "invalid"
        return answer
    elif (int(middle[1]) + int(middle[2]))%2 != 0:
        answer = "invalid"
        return answer
    elif (int(end[0]) + int(end[1]))%2 != 0:
        answer = "invalid"
        return answer
    else:
        answer = "valid"
    # for i in range(0,len(vowel)):
    for i in vowel:
        if tag[2] == i:
            answer = "invalid"
            return answer
    return answer

print (checktag(tag))    

