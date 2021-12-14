# 6
# -3 2 3 -4 3 1

def funclist (count,rangeofvalues,sum):
    for j in range (0,rangeofvalues):
        anew = a[i:]
        count = count + j
        countend = count + j+1
        if countend > rangeofvalues:
            listsum.append(sum)
            if listsum[0]>listsum[1]:
                del listsum[1]
            else:
                del listsum[0]
            return listsum
        listForSum = anew[count:countend]
        total = 0
        for k in listForSum:            
            total = total + int(k)
        sum = sum + total
    return listsum


n = int(input())
a = list(map(int,input().strip().split(" ")))
sum = 0
listsum = [0]
for i in range(0,n):
    count = 0
    index1 = 1
    rangeofvalues = n-i
    funclist (count,rangeofvalues,sum)
        
print (max(listsum))