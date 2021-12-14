a=input()
def palin(a):
    rangea = len(a)
    for i in range(0,rangea):
        if a[i] != a[rangea-1-i]:
            return "NO"
    return "YES"

print(palin(a))
