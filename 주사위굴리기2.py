n, n2, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cntList = [[0 for _ in range(n2)] for _ in range(n)]
dx = (0,1,0,-1)
dy = (1,0,-1,0)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n2

def dfs(arr):
    chk = [[0 for _ in range(n2)] for _ in range(n)]
    
    for x in range(n):
        for y in range(n2):
            if chk[x][y] == 0:
                cnt = 1
                li = []
                save = []
                li.append([x,y, arr[x][y]])
                save.append([x,y])
                chk[x][y] = 1
                while li:
                    xx, yy, color = li.pop()
                    
                    for i in range(4):
                        nx, ny = xx+dx[i], yy+dy[i]
                        if is_possible(nx, ny) and chk[nx][ny] == 0 and arr[nx][ny] == color:
                            cnt += 1
                            # print(nx, ny, color)
                            chk[nx][ny] = 1
                            li.append([nx,ny,color])                    
                            save.append([nx,ny])
                for s in save:
                    cntList[s[0]][s[1]] = cnt
                
dfs(grid)

d_center = 1
d_e, d_w, d_s, d_n = 3, 4, 5, 2 #동서남북

def mov(d):
    global d_center, d_e, d_w, d_s, d_n
    if d == 0:  # 오른쪽 이동
        d_e, d_center, d_w = d_center, d_w, 7-d_center
    elif d == 1: # 아래로 이동
        d_n, d_center, d_s = 7-d_center, d_n, d_center
    elif d == 2: # 왼쪽이동
        d_w, d_center, d_e = d_center, d_e, 7-d_center
    elif d == 3: # 위쪽이동
        d_n, d_center, d_s = d_center, d_s, 7-d_center

def turn(d):
    global d_center, d_e, d_w, d_s, d_n
    if d == 0:  #시계
        d_e, d_w, d_s, d_n = d_n, d_s, d_e, d_w
    elif d == 1: # 반시계
        d_e, d_w, d_s, d_n = d_s, d_n, d_w, d_e

# mov(0)

# print(cntList)

d = 0
x, y = 0, 0
ans = 0
for i in range(m):
    if not is_possible(x+dx[d], y+dy[d]):
        d = (d+2)%4
    mov(d)
    x += dx[d]
    y += dy[d]
    ans += cntList[x][y]*grid[x][y]

    # if i == 8 or i == 9:
    print("x:",x," y:",y)
    print(d_center,d)
    print(cntList[x][y], ans)
    print()

    if 7-d_center > grid[x][y]:
        d = (d+1)%4
    elif 7-d_center < grid[x][y]:
        d = (d+3)%4
    
    

print(ans)