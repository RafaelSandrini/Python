n = int(input())
x = list(map(int,input().strip().split(" ")))
if x[n-1]%10 == 0:
    print("Yes")
else:
    print("No")
