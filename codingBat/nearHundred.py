# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
    result = abs(100-n)
    result2 = abs(200-n)
    return (result <= 10 or result2 <=10)

print (near_hundred(93))
print (near_hundred(90))
print (near_hundred(89))
print (near_hundred(205))

