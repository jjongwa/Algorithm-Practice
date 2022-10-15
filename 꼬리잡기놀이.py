n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
team_grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            grid[i][j] = -1
        elif grid[i][j] == 4:
            grid[i][j] = 0

# grid 변경 확인
# for i in range(n):
#     print(*grid[i])
# print()

dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n

chk = [[0 for _ in range(n)] for _ in range(n)]

teamList = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            team_len = 1
            stack = [[i, j]]
            chk[i][j] = 1
            while stack:
                x, y = stack.pop()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if is_possible(nx, ny) and chk[nx][ny] == 0 and 0 < grid[nx][ny] < 4:
                        chk[nx][ny] = 1
                        stack.append([nx, ny])
                        team_len += 1
                        grid[nx][ny] = team_len
            teamList.append([team_len, i, j])

# for i in range(n):
#     print(*grid[i])
# print()
#
# print(teamList)
chk = [[0 for _ in range(n)] for _ in range(n)]
for t_l in teamList:
    i, j = t_l[1], t_l[2]
    team_grid[i][j] = t_l[0]
    stack = [[i, j]]
    chk[i][j] = 1
    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if is_possible(nx, ny) and chk[nx][ny] == 0 and grid[nx][ny] >= 0:
                chk[nx][ny] = 1
                team_grid[nx][ny] = t_l[0]
                stack.append([nx, ny])

print("teamgrid")
for i in range(n):
    print(*team_grid[i])
print()






def mov(arr):
    chk = [[0 for _ in range(n)] for _ in range(n)]
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == team_grid[i][j] and chk[i][j] == 0:
                stack = [[i, j, team_grid[i][j]]]
                while stack:
                    x, y, num = stack.pop()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if is_possible(nx, ny) and arr[nx][ny] == num-1:
                            tmp[nx][ny] = num
                            chk[nx][ny] = 1
                            stack.append([nx, ny, num-1])
    print("tmp")
    for i in range(n):
        print(*tmp[i])
    print()
    arr = [t[:] for t in tmp]



def turn(arr, tx, ty):
    global team_grid
    team_len = team_grid[tx][ty]
    # print(team_len)
    chk = [[0 for _ in range(n)] for _ in range(n)]
    chk[tx][ty] = 1
    arr[tx][ty] = team_len - arr[tx][ty] + 1
    stack = [[tx, ty]]

    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if is_possible(nx, ny) and arr[nx][ny] > 0 and chk[nx][ny] == 0:
                chk[nx][ny] = 1
                arr[nx][ny] = team_len - arr[nx][ny] +1
                stack.append([nx, ny])


ans = 0
for rnd in range(1, k+1):
    # 1. 이동
    mov(grid)

    # 2. 선 던지기
    way = (rnd-1) % (4*n)
    w_r, w_p = way // n, way % n

    if w_r == 0:
        x, y = w_p, 0
    elif w_r == 1:
        x, y = n-1, w_p
    elif w_r == 2:
        x, y = n-1-w_p, n-1
    elif w_r == 3:
        x, y = 0, w_p-n+1
    for i in range(n):
        nx, ny = x + dx[w_r] * i, y + dy[w_r] * i
        if grid[nx][ny] > 0:
            ans += grid[nx][ny] ** 2
            turn(grid, nx, ny)
            break

    # grid 변경 확인
    for i in range(n):
        print(*grid[i])
    print()
print(ans)
# turn(grid, 0, 1)





