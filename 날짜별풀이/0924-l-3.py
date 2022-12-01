from collections import deque
n, m = 3,3
fires = [[1, 1],[1,2]]
ices = [[3, 3]]

def sumMatrix(A,B):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]

def subMatrix(A,B):
    return [[c - d for c, d in zip(a, b)] for a, b in zip(A,B)]

def is_possible(x,y):
    return 0 <= x < n and 0 <= y < n





f_grid = [[[0 for _ in range(n)] for _ in range(n)]for _ in range(len(fires))]
i_grid = [[[0 for _ in range(n)] for _ in range(n)]for _ in range(len(ices))]

dx = (1,0,-1,0,1,-1,-1,1)
dy = (0,1,0,-1,1,1,-1,-1)
def bfs(arr, x, y, f_or_i):
    dq = deque()
    chk = [[0 for _ in range(n)] for _ in range(n)]
    dq.append([x,y])
    chk[x][y] = 1
    arr[x][y] = 1
    while dq:
        nowx, nowy = dq.popleft()
        for i in range(f_or_i):
            nx, ny = nowx+dx[i], nowy+dy[i]
            if is_possible(nx,ny) and chk[nx][ny] == 0:
                chk[nx][ny] = 1
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                else:
                    dq.append([nx,ny])

answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(1, m+1):
    sum_fire = [[0 for _ in range(n)] for _ in range(n)]
    sum_ice = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(len(fires)):
        bfs(f_grid[j], fires[j][0]-1,fires[j][1]-1, 8)
        sum_fire = sumMatrix(sum_fire,f_grid[j])

    for j in range(len(ices)):
        bfs(i_grid[j], ices[j][0]-1,ices[j][1]-1, 4)
        sum_ice = sumMatrix(sum_ice,i_grid[j])

    
    fire_last = 0
    ice_last = 0

    for x in range(n):
        for y in range(n):
            fire_last += sum_fire[x][y]
    
    for x in range(n):
        for y in range(n):
            ice_last += sum_ice[x][y]


    if fire_last %(n*n) == 0 and ice_last %(n*n) == 0:
        for k in range(n):
            for l in range(n):
                sum_fire[k][l] *= (m-i+1)
                sum_ice[k][l] *= (m-i+1)

        answer = sumMatrix(answer, subMatrix(sum_fire,sum_ice))
        break
    else:
        answer = sumMatrix(answer, subMatrix(sum_fire,sum_ice))
    
print(answer)