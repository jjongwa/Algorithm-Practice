n, m = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(n)]
chk = [[0 for _ in range(m)]for _ in range(n)]

'''
def jump(x, y, color, cnt):
    global chk
    for dx in range(1, n-x):
        nx = x+dx
        if grid[nx][y] != color:
            chk[nx][y] += cnt
            jump(nx, y, grid[nx][y], chk[nx][y])
    
    for dy in range(1, n-y):
        ny = y+dy
        if grid[x][ny] != color:
            chk[x][ny] += cnt
            jump(x, ny, grid[n][ny], chk[x][ny])
'''

def jump(x, y, color, cnt):
    global chk
    for dx in range(1, n-x):
        nx = x+dx
        for dy in range(1, m-y):
            ny = y+dy
            if grid[nx][ny] != color:
                chk[nx][ny] += cnt
                jump(nx, ny, grid[nx][ny], chk[nx][ny])


jump(0,0,grid[0][0], 1)

print(chk[n-1][m-1])

    