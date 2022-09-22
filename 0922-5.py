import sys
INT_MAX = sys.maxsize
N, M = map(int, input().split())
coin = list(map(int, input().split()))
coin.sort()
'''
dp  =[[INT_MAX for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    for j in range(M+1):
        if j >= coin[i]:
            dp[i][j] = min(dp[i-1][j-coin[i]]+1, dp[i-1][j])

        else:
            dp[i][j] = dp[i-1][j]

ans = dp[N][M]

if ans == INT_MAX:
    print(-1)
else:
    print(ans)
'''
dp = [INT_MAX] * (M+1)
dp[0] = 0

for i in  range(N):
    for j in range(M,-1,-1):
        if j-coin[i] >= 0 and dp[j-coin[i]] != INT_MAX:
            dp[j] = min(dp[j], dp[j-coin[i]]+1)
    # print(dp) 
print(dp)
if dp[M] == INT_MAX:
    print(-1)
else:
    print(dp[M])