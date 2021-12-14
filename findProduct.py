n = int(input())
a = list(map(int,input().strip().split(" ")))

result = 1
for i in a:
    result = result*i%(10**9+7)

print (result)

