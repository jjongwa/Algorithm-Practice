n, m, h, k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
thief = []
tree = []
cx, cy = n//2, n//2
tdx = (0, 1, 0, -1)
tdy = (1, 0, -1, 0)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n
for _ in range(m):
    tx, ty, td = map(int, input().split())  # 도망자 위치와 방향
    thief.append([tx-1, ty-1, td-1])
for _ in range(h):
    tx, ty = map(int, input().split())
    tree.append([tx-1, ty-1])

def mov_thief():
    for th in thief:
        if abs(th[0]-cx) + abs(th[1]-cy) <=3:
            nx, ny = th[0] + tdx[th[2]], th[1] + tdy[th[2]]
            if is_possible(nx, ny):
                if cx == nx and cy == ny:
                    continue
                else:
                    th[0], th[1] = nx, ny
            else:
                th[2] = (th[2] + 2) % 4
                nx, ny = th[0] + tdx[th[2]], th[1] + tdy[th[2]]
                if is_possible(nx, ny):
                    if cx == nx and cy == ny:
                        continue
                    else:
                        th[0], th[1] = nx, ny

ans = 0
# print(thief)

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
cd = 0
now_len = 0
max_len = 1
len_step = 0
c_reverse = 0
for turn in range(1, k+1):
    mov_thief() # 도둑 움직임

    #   술래 움직임
    if c_reverse == 0:
        cx, cy = cx+dx[cd], cy+dy[cd]
        now_len += 1
        if now_len == max_len:
            cd = (cd+1) % 4
            len_step += 1
            now_len = 0
        if len_step == 2:
            max_len += 1
            len_step = 0
        if cx == 0 and cy == 0:
            c_reverse = 1
            cd = 2
            now_len = 0
            max_len = 4
            len_step = -1
    elif c_reverse == 1:
        cx, cy = cx + dx[cd], cy + dy[cd]
        now_len += 1
        if now_len == max_len:
            cd = (cd + 3) % 4
            len_step += 1
            now_len = 0
        if len_step == 2:
            max_len -= 1
            len_step = 0
        if cx == n//2 and cy == n//2:
            cd = 0
            now_len = 0
            max_len = 1
            len_step = 0
            c_reverse = 0

    # 술래 잡기
    # print(thief)
    # print(cx, cy, cd)

    del_list = []
    die_thief = []
    for ii in range(3):
        fx = cx + dx[cd]*ii
        fy = cy + dy[cd]*ii
        if is_possible(fx, fy) and [fx, fy] not in tree:    # 가능한 위치고 트리가 없을 떄
            for th in thief:
                if th[0] == fx and th[1] == fy:
                    die_thief.append(th)

    # print(die_thief)
    ans += (len(die_thief) * turn)

    new_thief = []
    for tt in thief:
        if tt not in die_thief:
            new_thief.append(tt)

    thief = new_thief[:]

print(ans)
# print(tree)
# print()
# for i in range(n):
#     print(*grid[i])