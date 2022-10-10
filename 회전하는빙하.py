import copy
from collections import deque
n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]
r_level = list(map(int, input().split()))

def is_possible(x, y):
    return 0 <= x < 2**n and 0 <= y < 2**n

def do_rotate(arr, L):
    for i in range(0, 2**n, 2**L):
        for j in range(0, 2**n, 2**L):
            # print(i, j )
            rotate(arr, i,j,L)



def rotate(arr, x, y, L):
    for i in range(2**(L-1)):
        for j in range(2**(L-1)):
            # print(x,y, x+i, y+j)
            
            # print(arr[x+i][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j], arr[x+i][y+j])
            # print(arr[x+i][y+j], arr[x+i][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j])
            # print()
            arr[x+i][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j], arr[x+i][y+j] \
            = arr[x+i][y+j], arr[x+i][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j+(2**(L-1))], arr[x+i+(2**(L-1))][y+j]

dx = (0, 1, 0 ,-1)
dy = (1, 0, -1, 0)

def melt():
    global grid
    tmp = copy.deepcopy(grid)
    for x in range(2**n):
        for y in range(2**n):
            cnt = 0
            if grid[x][y] == 0:
                continue
            for i in range(4):
                nx , ny = x+dx[i], y+dy[i]
                if is_possible(nx,ny) and grid[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                tmp[x][y] -= 1
    grid = tmp

# print()
for qq in r_level:
    # print(qq)
    if 0 < qq <= n:
        do_rotate(grid, qq)
    melt()

    # for i in range(2**n):
    #     print(*grid[i])
    # print()


ans = 0
for i in range(2**n):
    ans += sum(grid[i])
print(ans)

max_ans = 0
check = [[0 for _ in range(2**n)] for _ in range(2**n)]

dq = deque()
for i in range(2**n):
    for j in range(2**n):
        if grid[i][j] != 0 and check[i][j] == 0:
            dq.appendleft([i, j])
            check[i][j] = 1
            cntt = 1
            while dq:
                x, y = dq.pop()                
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if is_possible(nx,ny) and grid[nx][ny] != 0 and check[nx][ny] == 0:
                        dq.appendleft([nx,ny])
                        check[nx][ny] = 1
                        cntt+=1
            max_ans = max(max_ans, cntt)

print(max_ans)



