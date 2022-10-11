dxs = (0,-1,-1,-1,0,1,1,1)
dys = (1,1,0,-1,-1,-1,0,1)

n , m = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

liv = [[0 for _ in range(n)] for _ in range(n)]
liv[n-2][0], liv[n-1][0], liv[n-2][1], liv[n-1][1] = 1, 1, 1, 1

def is_possible(x,y):
    return 0 <= x < n and 0 <= y < n

def mov(d, p):
    global liv
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if liv[i][j] == 1:
                x, y = i, j
                for _ in range(p):
                    x, y = x+dxs[d-1], y+dys[d-1]
                    if x <0:
                        x+=n
                    elif x >= n:
                        x -= n
                    if y <0:
                        y+=n
                    elif y >= n:
                        y -= n
                tmp[x][y] = 1

    liv = [t[:] for t in tmp]

def grow():
    global liv
    global grid

    for x in range(n):
        for y in range(n):
            if liv[x][y] == 1:
                grid[x][y] += 1
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if liv[x][y] == 1:
                for i in range(1,8,2):
                    nx, ny = x+dxs[i], y+dys[i]
                    if is_possible(nx,ny) and grid[nx][ny] >0:
                        grid[x][y] += 1
    for x in range(n):
        for y in range(n):
            if liv[x][y] == 0 and grid[x][y] >= 2:
                grid[x][y] -= 2
                tmp[x][y] = 1

    liv = [t[:] for t in tmp]
                
            



for _ in range(m):
    d, p = map(int, input().split())
    mov(d,p)
    grow()

ans = 0
for i in range(n):
    ans += sum(grid[i])


# mov(d,p)
# grow()

    for i in range(n):
        print(*grid[i])
    print()
    for i in range(n):
        print(*liv[i])
    print()

print(ans)