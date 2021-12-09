T = int(input())
result = []
totalGreen = 0
totalPurple = 0

for j in range(0,T):
    cost = []
    valueGreen = 0
    valuePurple = 0
    cost = list(map(str,input().strip().split(" ")))
    if j%2 != 0:
        valueGreen = cost[0]
        valuePurple = cost[1]
    else:
        valueGreen = cost[1]
        valuePurple = cost[0]
    n = int(input())
    total = 0
    totalGreen = 0
    totalPurple = 0
    for i in range(0,n):
        price = list(map(int,input().strip().split(" ")))
        totalGreen = int(valueGreen) * (int(price[0]))
        totalPurple = int(valuePurple) * (int(price[1]))
        total = total + totalGreen + totalPurple
        price = []
    result.append(total)

for i in result:
    print (i)
