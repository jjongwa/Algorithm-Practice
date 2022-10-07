import copy
TAGGER = [-2, -2]
BLANK = [-1, -1]

grid = []
for _ in range(4):
    inp = list(map(int, input().split()))
    grid.append([[inp[0], inp[1]-1], [inp[2], inp[3]-1], [inp[4], inp[5]-1],[inp[6], inp[7]-1]])

dxs = [-1, -1,  0,  1, 1, 1, 0, -1]
dys = [ 0, -1, -1, -1, 0, 1, 1,  1]

def is_possible(x,y):
    return 0 <= x < 4 and 0 <= y < 4

def th_can_go(x,y):
    return is_possible(x,y) and grid[x][y] != TAGGER

def ta_can_go(x,y):
    return is_possible(x,y) and grid[x][y] != BLANK

def done(x, y, d):
    for dist in range(1, 4):
        nx, ny = x + dxs[d]*dist, y + dys[d]*dist
        if ta_can_go(nx, ny):
            return False
    return True

def get_next(x, y, d):
    for r in range(8):
        n_d = (d+r) % 8
        nx, ny = x + dxs[n_d], y +dys[n_d]
        if th_can_go(nx, ny):
            return (nx, ny, n_d)

    return (x, y, d)

def swap(x, y, nx, ny):
    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]

def mov(t_num):
    for x in range(4):
        for y in range(4):
            n, d = grid[x][y]
            if n == t_num:
                nx, ny, nd = get_next(x,y,d)
                grid[x][y] = [n, nd]
                swap(x, y, nx, ny)
                return

def cycle():
    for i in range(1, 17):
        mov(i)

def search_max_score(x, y, d, score):
    global max_score
    global grid

    if done(x, y, d):
        max_score = max(max_score, score)
        return

    for dist in range(1, 5):
        nx, ny = x + dxs[d]*dist, y + dys[d]*dist

        if not ta_can_go(nx, ny):
            continue

        tmp = copy.deepcopy(grid)

        ex_score, nd = grid[nx][ny]
        grid[nx][ny], grid[x][y] = TAGGER, BLANK

        cycle()

        search_max_score(nx, ny, nd, score + ex_score)

        grid = copy.deepcopy(tmp)

st_score, st_d = grid[0][0]
grid[0][0] = TAGGER

cycle()

max_score = 0

search_max_score(0,0,st_d, st_score)
print(max_score)

# from collections import deque
# import copy
# grid = []
# for _ in range(4):
#     inp = list(map(int, input().split()))
#     grid.append([[inp[0], inp[1]], [inp[2], inp[3]], [inp[4], inp[5]],[inp[6], inp[7]]])


# # for i in range(4):
# #     print(*grid[i])
# # print()

# def is_possible(x,y):
#     return 0 <= x < 4 and 0 <= y < 4

# def nxt_p(x,y,d):
#     if d == 1:
#         return (x-1,y)
#     elif d == 2:
#         return (x-1,y-1)
#     elif d == 3:
#         return (x,y-1)
#     elif d == 4:
#         return (x+1,y-1)
#     elif d == 5:
#         return (x+1,y)
#     elif d == 6:
#         return (x+1,y+1)
#     elif d == 7:
#         return (x,y+1)
#     elif d == 8:
#         return (x-1,y+1)

# def mov(x,y,d, arr):
#     nd = d
#     while True:
#         nx, ny = nxt_p(x,y,nd)
#         if is_possible(nx,ny) and arr[nx][ny] != [0,0]:
#             arr[x][y][1] = nd
#             tmp = arr[x][y]
#             arr[x][y] = arr[nx][ny]
#             arr[nx][ny] = tmp
#             break
#         nd += 1
#         if nd == 9:
#             nd =1
#         if nd == d:
#             break

# def cycle(arr):
#     for n in range(1,17):
#         tri = 0
#         for i in range(4):
#             for j in range(4):
#                 if arr[i][j][0] == n:
#                     mov(i,j,arr[i][j][1], arr)
#                     tri = 1
#             if tri == 1:
#                 break

# ansList = []
# cnt, di = grid[0][0][0], grid[0][0][1]
# grid[0][0] = [0,0]
# cycle(grid)

# dq = deque()
# dq.append([grid, cnt, 0, 0, di])



# while dq:
#     now_grid, now_cnt, x, y, now_di = dq.popleft()
#     ansList.append(now_cnt)
#     # for i in range(4):
#     #     print(*now_grid[i])
#     # print()
#     while is_possible(nxt_p(x,y,now_di)[0], nxt_p(x,y,now_di)[1]):
#         nx, ny = nxt_p(x,y,now_di)
#         if now_grid[nx][ny] != [0,0]:
#             tmp_grid = copy.deepcopy(now_grid)
#             nxt_cnt = now_cnt + tmp_grid[nx][ny][0]
#             nxt_di = tmp_grid[nx][ny][1]
#             tmp_grid[nx][ny] = [0,0]
#             # print(nx, ny, nxt_di, nxt_cnt)
#             for i in range(4):
#                 print(*tmp_grid[i])    
#             print()     
#             cycle(tmp_grid)
#             for i in range(4):
#                 print(*tmp_grid[i])    
#             print()   
#             dq.append([tmp_grid, nxt_cnt, nx, ny, nxt_di])
            
#             for i in range(4):
#                 print(*tmp_grid[i])    
#             print()        
#         x, y = nx, ny


# # for i in range(4):
# #     print(*grid[i])

# print(ansList)
# print(max(ansList))