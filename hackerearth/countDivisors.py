a = list(map(int,input().strip().split()))
rangea = range(a[0],a[1]+1)
count = 0
for i in rangea:
    if i%a[2] == 0:
        count += 1
print (count)