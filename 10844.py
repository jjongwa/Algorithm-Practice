# 쉬운 계단 수
ansList = [[0,0,0,0,0,0,0,0,0,0] for _ in range(101)]
ansList[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2,len(ansList)):
    ansList[i][0] = ansList[i-1][1]
    ansList[i][1] = ansList[i-1][0] + ansList[i-1][2] 
    ansList[i][2] = ansList[i-1][1] + ansList[i-1][3] 
    ansList[i][3] = ansList[i-1][2] + ansList[i-1][4]
    ansList[i][4] = ansList[i-1][3] + ansList[i-1][5]
    ansList[i][5] = ansList[i-1][4] + ansList[i-1][6]
    ansList[i][6] = ansList[i-1][5] + ansList[i-1][7]
    ansList[i][7] = ansList[i-1][6] + ansList[i-1][8]
    ansList[i][8] = ansList[i-1][7] + ansList[i-1][9]
    ansList[i][9] = ansList[i-1][8] 
 
N = int(input())
print(sum(ansList[N])% 1000000000)
