n, m = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(n)]
cnt = 0

def dfs(x, y, c):
    global cnt

    for i in range(1, n-x):
        for j in range(1, m-y):
            nx, ny = x+i, y+j
            if grid[nx][ny] != c:
                if nx == n-1 and ny == m-1:
                    cnt += 1
                else:
                    dfs(nx, ny, grid[nx][ny])

dfs(0,0,grid[0][0])

print(cnt % 10007)