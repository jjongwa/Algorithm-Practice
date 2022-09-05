dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_possible(x,y):
    return 0 <= x < n and  0 <= y < n

n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
chk = [[0 for _ in range(n)] for _ in range(n)]
r -= 1
c -= 1
ansList = [grid[r][c]]
chk[r][c] = 1

tri = 0
while True:
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if is_possible(nx,ny) and grid[r][c] < grid[nx][ny] and chk[nx][ny] == 0:
            chk[nx][ny] = 1
            ansList.append(grid[nx][ny])
            r, c = nx, ny
            break
        if i == 3:
            tri = 1
    if tri == 1:
        break

print(*ansList)