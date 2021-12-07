n = int(input())
village = input()
def villagecheck (n,village):
    newvillage = ""
    for i in range(0,n-1):
        if village[i]=="H" and village[i]==village[i+1]:
            return "NO"
    newvillage = village.replace (".","B")
    print ("YES")
    return (newvillage)   

print (villagecheck(n,village))