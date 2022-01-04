n = int(input())
ansList = [0,1,2]+[0]*999
for i in range(3,len(ansList)):
    ansList[i] = ansList[i-1] + ansList[i-2]
    if ansList[i] >10007:
        ansList[i] %= 10007

print(ansList[n])


