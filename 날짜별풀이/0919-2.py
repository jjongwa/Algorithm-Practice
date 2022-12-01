n = int(input())
numList = list(map(int,input().split()))
dic = {}
for i in numList:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

tri = 0
for a in dic:
    if dic[a] == 1:
        print(a)
        tri = 1
        break
if tri == 0:
    print(-1)