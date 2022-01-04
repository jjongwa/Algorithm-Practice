#   ÇÕºÐÇØ
'''
ansList = [[0]* 201 for _ in range(201)]
ansList[0][0] = 1
N, K = map(int,input().split())
for i in range(0,N+1):
    for j in range(1,K+1):
        ansList[i][j] = ansList[i-1][j] + ansList[i][j-1]

print(ansList[N][K] % 1000000000)
'''

import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[1]*(N) for i in range(K)]
dp[1][0] = 2
for i in range(1,K):
    dp[i][0] = i+1
    for j in range(1,N):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
print(dp[K-1][N-1]%1000000000)