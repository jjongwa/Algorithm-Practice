from itertools import combinations
S = int(input())
numList = list(map(int,input().split()))
#print(numList)
ansList = []
for i in range(S):
    combi = combinations(numList, i+1)
    for j in combi:
        ansList.append(sum(j))
        #print(i, j)
ansList.sort()

for i in range(len(ansList)):
    if i == 0 and ansList[i] > 1:
        print(1)
        break
    elif i != 0 and ansList[i-1]+1 < ansList[i]:
            print(ansList[i-1]+1)
            break
    if i == len(ansList)-1:
        print(ansList[i]+1) 
print(ansList)