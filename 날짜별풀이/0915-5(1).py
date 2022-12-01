n, m = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(n)]
cnt = 0

dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(m):
        for k in range(i):
            for l in range(j):
                if grid[k][l] != grid[i][j]:
                    dp[i][j] = (dp[i][j] + dp[k][l]) % 10007

print(dp[n-1][m-1])
