# PARTIALLY CORRECT

# n = int(input())
# a = list(map(int,input().strip().split(" ")))
# b = list(map(int,input().strip().split(" ")))

# count = 0
# minValue = min(a)
# for i in range(0,n):    
#     if a[i] != minValue:
#         while a[i] != minValue:
#             a[i]=a[i]-b[i]
#             count += 1
#             if a[i]<minValue:
#                 count = -1
#                 break

# print (count)

n = int(input())
a = list(map(int,input().strip().split(" ")))
b = list(map(int,input().strip().split(" ")))

def numberSteps(n,a,b):
    count = 0
    minValue = min(a)
    for i in range(n):    
        if a[i] > minValue:
            if a[i]<b[i]:
                count = -1
                return count
            else:
                while a[i] > minValue:
                    a[i]=a[i]-b[i]
                    count += 1
                    if a[i]<minValue:
                        count = -1
                        return count
    return count

print (numberSteps(n,a,b))