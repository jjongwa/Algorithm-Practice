from collections import deque
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y, c):
    cnt = 1
    dq = deque()
    dq.append([x,y])
    grid[x][y] = c
    while dq:
        nowx, nowy = dq.popleft()                
        for i in range(4):
            nx, ny = nowx+dx[i], nowy+dy[i]
            if is_possible(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
                dq.append([nx,ny])
                grid[nx][ny] = c
    return cnt

chk = 2
vil = {}
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            vil[chk] = bfs(i,j, chk)
            chk += 1

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            near = []
            tmp = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if is_possible(nx,ny) and grid[nx][ny] != 0 and grid[nx][ny] not in near:
                    near.append(grid[nx][ny])
            for ne in near:
                tmp += vil[ne]
            ans = max(ans,tmp)

print(ans+1)