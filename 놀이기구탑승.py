n = int(input())
likeList = {}
grid = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n*n):
    n0, n1, n2, n3, n4 = map(int, input().split())
    likeList[n0] = [n1, n2, n3, n4]
# print(likeList)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n

for nn in likeList:
    likespot = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                empty, person = 0,0
                for k in range(4):
                    nx, ny = i+ dx[k], j + dy[k]
                    if is_possible(nx,ny):
                        if grid[nx][ny] in likeList[nn]:
                            person += 1
                        elif grid[nx][ny] == 0:
                            empty += 1
                likespot.append([person, empty, i, j])
    likespot.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    
    grid[likespot[0][2]][likespot[0][3]] = nn

ans = 0
for x in range(n):
    for y in range(n):
        chk = 0

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if is_possible(nx,ny) and grid[nx][ny] in likeList[grid[x][y]]:
                chk += 1
        if chk != 0:
            ans += 10**(chk-1)

print(ans)

print(grid)

