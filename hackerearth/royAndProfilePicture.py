l = int(input())
n = int(input())
answers = []



for i in range(0,n):
    a = list(map(int,input().strip().split()))
    if a[0]<l or a[1]<l:
        answers.append("UPLOAD ANOTHER")
    else:
        if  a[0] == a[1]:
            answers.append("ACCEPTED")
        else:
            answers.append("CROP IT")

for i in answers:
    print (i)