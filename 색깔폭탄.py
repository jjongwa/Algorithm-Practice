import copy
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

red = []
point = 0
dx = (1, 0 ,-1, 0)
dy = (0, 1, 0, -1)

def is_possible(x,y):
    return 0 <= x < n and 0 <= y < n

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            red.append([i, j])


def bombgrid():
    global point
    global red
    chk = [[0 for _ in range(n)] for _ in range(n)]
    bombList = []
    for cc in range(1,m+1):
        c_cnt = 0
        tmpList = []
        for x in range(n-1,-1,-1):
            for y in range(n-1,-1,-1):
                if grid[x][y] != -2  and grid[x][y] != -1 and grid[x][y] != 0 and chk[x][y] == 0:
                    # print("dsd",x, y)
                    c = grid[x][y]
                    c_cnt += 1
                    cnt = 0
                    chkred = 0
                    dq = deque()
                    chk[x][y] = 1
                    dq.append([x, y])
                    while dq:
                        cnt += 1
                        xx, yy =dq.popleft()
                        for i in range(4):
                            nx, ny = xx+dx[i], yy+dy[i]
                            if is_possible(nx, ny) and chk[nx][ny] == 0:
                                if grid[nx][ny] == c:
                                    dq.append([nx,ny])
                                    chk[nx][ny] = 1
                                if grid[nx][ny] == 0:
                                    dq.append([nx,ny])
                                    chk[nx][ny] = 1
                                    chkred += 1
                    # print(tmpList)
                    if cnt >1:
                        bombList.append([cnt, chkred, x, y, c])
        # if len(tmpList) == 1 and tmpList[0][0] >1:
        #     bombList.append(tmpList[0])
        
        
        

                for r in red:
                    chk[r[0]][r[1]] = 0
                # for i in range(n):
                #     print(*chk[i])
                # print()
    bombList.sort(key=lambda x :(-x[0], -x[1], -x[2], -x[3]))
    # print(bombList)
    if len(bombList) == 0:
        return -1
    
    b_cnt, b_red, b_x, b_y, b_c = bombList[0]

    point += b_cnt**2   # 포인트
    chk = [[0 for _ in range(n)] for _ in range(n)] #폭파위해 초기화
    dq = deque()
    chk[b_x][b_y] = 1
    dq.append([b_x, b_y])
    while dq:                        
        xx, yy =dq.popleft()
        grid[xx][yy] = -2
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if is_possible(nx, ny) and chk[nx][ny] == 0:
                if grid[nx][ny] == b_c or grid[nx][ny] == 0:
                    dq.append([nx,ny])
                    chk[nx][ny] = 1                                                                
    return 0
def gravity():
    global red
    for x in range(n-2, -1, -1):
        for y in range(n):
            if 0 <=grid[x][y] <=m :
                i = 1
                while True:                    
                    if is_possible(x+i, y) and grid[x+i][y] == -2:
                        i+=1
                    else:
                        break
                    # print(i)
                grid[x][y], grid[x+i-1][y] = grid[x+i-1][y], grid[x][y]
    tmp =[]
    for ii in range(n):
        for jj in range(n):
            if grid[ii][jj] == 0:
                tmp.append([ii,jj])
    red = copy.deepcopy(tmp)

def turn():
    global grid
    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[n-1-j][i] = grid[i][j]
    grid = copy.deepcopy(tmp)

# tri = bombgrid()
    
# gravity()
# turn()
# gravity()


while True:
    tri = bombgrid()
    if tri == -1:
        break
    gravity()
    turn()
    gravity()




    
    # for i in range(n):
    #     print(*grid[i])


print(point)
    # print()
