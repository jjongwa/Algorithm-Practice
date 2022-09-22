n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def is_possible(x, y):
    return 0<= x < n and 0 <= y < n

def find(x,y):
    if dp[x][y] != -1:
        return
    way = []
    for i in range(4):
        nx, ny = x+dx[i], y + dy[i]
        if is_possible(nx,ny) and grid[nx][ny] > grid[x][y]:
            if dp[nx][ny] == -1:
                find(nx, ny)    
            way.append(dp[nx][ny])
    if len(way):
        dp[x][y] = max(way) + 1
    else:
        dp[x][y] = 1

for i in range(n):
    for j in range(n):
        find(i,j)

ans = 0
for i in range(n):
    ans = max(ans, max(dp[i]))
print(ans)