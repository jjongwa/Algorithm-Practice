N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]


# dp[i]가 무엇인지 정의
# 점화식
# 초기조건, 종료조건

# 격자니까 dp[i][j]
# dp[i][j] : 마지막으로 방문한 위치가 (i,j)일 때, 얻을 수 있는 최대 합
dp[0][0] = grid[0][0]
def chk(x,y):
    if dp[x][y] != 0:
        return dp[x][y]
    if x == 0 and y == 0:
        return grid[0][0]
    elif x == 0:
        dp[x][y] = grid[x][y] + chk(x,y-1)
        return dp[x][y]
    elif y == 0:
        dp[x][y] = grid[x][y] + chk(x-1,y)
        return dp[x][y]
    
    dp[x][y] = grid[x][y] + max(chk(x,y-1), chk(x-1,y))

    return dp[x][y]

print(chk(N-1,N-1))
print(dp)