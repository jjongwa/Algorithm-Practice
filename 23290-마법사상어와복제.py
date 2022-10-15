from collections import deque
grid = [[[] for _ in range(4)] for _ in range(4)]
m, t = map(int, input().split())

for _ in range(m):
    mx, my, d = map(int, input().split())
    grid[mx-1][my-1].append([1,d])

r, c = map(int, input().split())
r, c = r-1, c-1
grid[r][c].append([-1,-1])

dxs = (0, -1, -1, -1, 0, 1, 1, 1)
dys = (-1, -1, 0, 1, 1, 1, 0, -1)

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

def is_possible(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def dfs(arr, x, y, cnt, chk, lim):
    global comp_eat
    global max_eat
    if lim == 3:
        comp_eat.append([cnt, chk])
        max_eat = max(max_eat, cnt)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if is_possible(nx, ny) and [nx, ny] not in chk:
            n_chk = chk[:]
            n_chk.append([nx,ny])
            dfs(arr, nx, ny, cnt+len(arr[nx][ny]), n_chk, lim+1)



for _ in range(t):
    egg = []
    n_grid = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for cc in grid[i][j]:
                if cc[0] == 1:
                    egg.append([i, j, cc[1]])
                    n_grid[i][j].append([1, cc[1]])
                    for dd in range(8):
                        nd = cc[1] - dd - 1
                        if nd < 0:
                            nd += 8
                        nx, ny = i+dxs[nd], j+dys[nd]
                        if is_possible(nx, ny):
                            is_ok = 1
                            for ccc in grid[nx][ny]:
                                if ccc[0] == -1 or ccc[0] == 2:
                                    is_ok = 0
                                    break
                            if is_ok:
                                n_grid[nx][ny].append([1, nd+1])
                                n_grid[i][j].pop()
                                break

    # for i in range(4):
    #     print(*n_grid[i])
    # print()
    # grid = [[ttt[:] for ttt in tt] for tt in n_grid]
    # 팩맨 이동
    comp_eat = []
    max_eat = 0
    dfs(n_grid, r, c, 0, [], 0)
    ghost =[]
    # print(comp_eat)
    for ce in comp_eat:
        if ce[0] == max_eat:
            r, c = ce[1][2][0], ce[1][2][1]
            # print(ce)
            # print(r, c)
            # print()
            # 팩맨 이동시키기
            for g in ce[1]:
                ln = len(n_grid[g[0]][g[1]])
                for _ in range(ln):
                    ghost.append([g[0], g[1]])
                    n_grid[g[0]][g[1]].pop()
            n_grid[r][c].append([-1, -1])
            break

    # 시체 소멸 및 고스트 복사
    for i in range(4):
        for j in range(4):
            for cc in grid[i][j]:
                if cc[0] == 2 and cc[1] == 0:
                    n_grid[i][j].append([2, 1])
    for g in ghost:
        n_grid[g[0]][g[1]].append([2, 0])

    # 알 부화
    for eg in egg:
        n_grid[eg[0]][eg[1]].append([1, eg[2]])

    grid = [[ttt[:] for ttt in tt] for tt in n_grid]
    # grid[0][0].append("gfaf")
    # print(egg)
    # print()
    # for i in range(4):
    #     print(*n_grid[i])
    # print()
# print()
# for i in range(4):
#     print(*grid[i])

ans = 0
for i in range(4):
    for j in range(4):
        for c in grid[i][j]:
            if c[0] == 1:
                ans += 1
print(ans)