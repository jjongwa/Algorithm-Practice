
INf = float('inf')

N = int(input())
house = []
for i in range(N):
    house.append(list(map(int,input().split())))

ansList = []

for i in range(3):
    tmp = [[0,0,0] for _ in range(N)]
    for  j in range(3):
        if j == i:
            tmp[0][j] = house[0][j]
            continue
        tmp[0][j] = INf

    for j in range(1,N):
        tmp[j][0] = min(tmp[j-1][1], tmp[j-1][2]) + house[j][0]
        tmp[j][1] = min(tmp[j-1][0], tmp[j-1][2]) + house[j][1]
        tmp[j][2] = min(tmp[j-1][0], tmp[j-1][1]) + house[j][2]
        
    for j in range(3):
        if j == i:
            continue
        ansList.append(tmp[-1][j])

print(min(ansList))


'''
INF = float('inf')
n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int,input().split())))
minVal = INF

for i in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]

    for j in range(3):
        if i == j:
                dp[0][j] = cost[0][j]
                continue
        dp[0][j] = INF

    for j in range(1,n):
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if j == i:
            continue
        minVal = min(minVal, dp[-1][j])
print(minVal)
'''