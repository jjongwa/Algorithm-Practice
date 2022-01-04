#   오르막 수
N = int(input())
ansList = [[0,0,0,0,0,0,0,0,0,0] for _ in range(N+1)]
ansList[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2,N+1):
    for j in range(10):
        for k in range(0,j+1):
            ansList[i][j] = (ansList[i][j] + ansList[i-1][k] ) % 10007

#print(ansList)

print(sum(ansList[N])% 10007)