n = int(input())
a = list(map(str,input().strip().split(" ")))
first = a[:n//2]
last = a[((n//2)):]
result = ""
for i in first:
    result = result + str(i[0])
for i in last:
    result = result + str(i[-1])

print (result)
