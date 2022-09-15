dx = [-1,1,0,0]
dy = [0,0,-1,1]


def is_possible(x,y):
    return 0<= x < n and 0 <= y <n

n, m, t = map(int,input().split())
cnt = [[0 for _ in range(n)] for _ in range(n)]
n_cnt = [[0 for _ in range(n)] for _ in range(n)]
grid = [list(map(int,input().split())) for _ in range(n)]
for _ in range(m):
    x, y = map(int,input().split())
    cnt[x-1][y-1] = 1

def mov():
    global cnt, n_cnt
    for x in range(n):
        for y in range(n):
            if cnt[x][y] == 1:
                best = 0
                bestgrid = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if is_possible(nx,ny):                        
                        if bestgrid != max(bestgrid,grid[nx][ny]):
                            best = i
                            bestgrid = max(bestgrid,grid[nx][ny])
                n_cnt[x+dx[best]][y+dy[best]] += 1
                        
    cnt = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if n_cnt[x][y] ==  1:
                cnt[x][y] = 1
    n_cnt = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(t):
    mov()

ans = 0
for i in range(n):
    for j in range(n):
        ans += cnt[i][j]
print(ans)