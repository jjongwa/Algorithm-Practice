import sys
INT_MAX = sys.maxsize
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[INT_MAX for _ in range(N)] for _ in range(N)]


dp[0][N-1] = grid[0][N-1]
def chk(x,y):
    if dp[x][y] != INT_MAX:
        return dp[x][y]
    if x == 0 and y == N-1:
        return grid[0][N-1]
    elif x == 0:
        dp[x][y] = grid[x][y] + chk(x,y+1)
        return dp[x][y]
    elif y == N-1:
        dp[x][y] = grid[x][y] + chk(x-1,y)
        return dp[x][y]
    
    dp[x][y] = grid[x][y] + min(chk(x,y+1), chk(x-1,y))

    return dp[x][y]

print(chk(N-1,0))
print(dp)