#   ÀÌÁø¼ö
ansList = [[0,0] for _ in range(91)]
ansList[1] = [0,1]
for i in range(2,len(ansList)):
    ansList[i][0] = ansList[i-1][1] +ansList[i-1][0] 
    ansList[i][1] = ansList[i-1][0]

N = int(input())
print(sum(ansList[N]))