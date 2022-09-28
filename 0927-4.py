from collections import deque
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = (1, 0 ,-1, 0)
dy = (0, 1, 0, -1)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    dq = deque()
    dq.append([x, y, 0])
    chk = [[0]*(n) for _ in range(n)] 
    chk[x][y] = 1
    while dq:
        nowx,nowy, dist = dq.popleft()

        for i in range(4):
            nx, ny = nowx + dx[i], nowy + dy[i]
            if is_possible(nx,ny) and chk[nx][ny] == 0 and grid[nx][ny] != 1:
                if grid[nx][ny] == 0:
                    chk[nx][ny] = 1
                    dq.append((nx, ny, dist+1))
                elif grid[nx][ny] == 2:
                    return dist+1

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            ans = max(ans, bfs(i,j)//2)
print(ans)
        