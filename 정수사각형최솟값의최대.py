import sys
INT_MAX = sys.maxsize
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[INT_MAX for _ in range(N)] for _ in range(N)]
dp[0][0] = grid[0][0]

def path(x,y):
    if dp[x][y] != INT_MAX:
        return dp[x][y]
    if x == 0:
        dp[x][y] = min(grid[x][y], path(x,y-1))
        return dp[x][y]
    if y == 0:
        dp[x][y] = min(grid[x][y], path(x-1,y))
        return dp[x][y]
    
    dp[x][y] = min(grid[x][y], max(path(x-1,y), path(x,y-1)))
    return dp[x][y]
print(path(N-1,N-1))
print(dp)