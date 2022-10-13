n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)


def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n


def get_list():
    li = []
    max_len, now_len = 1, 0
    ro_cnt = 0
    di = 0
    x, y = n // 2, n // 2 - 1
    while is_possible(x, y):
        if grid[x][y] != 0:
            li.append(grid[x][y])
        now_len += 1
        if max_len == now_len:
            di = (di + 1) % 4
            ro_cnt += 1
            now_len = 0
        if ro_cnt == 2:
            ro_cnt = 0
            max_len += 1
        x += dx[di]
        y += dy[di]
    return li


def kill(lii):
    global ans
    global one, two, thr
    new_li = [lii[0]]
    now_num = lii[0]
    num_cnt = 1
    for l in range(1, len(lii)):
        if lii[l] != lii[l - 1]:
            if num_cnt >= 4:
                for _ in range(num_cnt):
                    number = new_li.pop()
                    if number == 1:
                        one += 1
                    elif number == 2:
                        two += 1
                    elif number == 3:
                        thr += 1
            num_cnt = 1
            now_num = lii[l]
        else:
            num_cnt += 1
        new_li.append(lii[l])
        # print(new_li)

    if num_cnt >= 4:
        for _ in range(num_cnt):
            number = new_li.pop()
            if number == 1:
                one += 1
            elif number == 2:
                two += 1
            elif number == 3:
                thr += 1
    return new_li


def remake(li):
    new_li = []
    now_num = li[0]
    now_cnt = 1
    for i in range(1, len(li)):
        if now_num != li[i]:
            new_li.append(now_cnt)
            new_li.append(now_num)
            now_num = li[i]
            now_cnt = 1
        else:
            now_cnt += 1
    new_li.append(now_cnt)
    new_li.append(now_num)
    return new_li


def fill(li):
    new_li = [[0 for _ in range(n)] for _ in range(n)]
    max_len, now_len = 1, 0
    ro_cnt = 0
    cnt = 0
    di = 0
    x, y = n // 2, n // 2 - 1
    while is_possible(x, y) and cnt < len(li):
        # print(x, y)
        new_li[x][y] = li[cnt]
        cnt += 1
        now_len += 1
        if max_len == now_len:
            di = (di + 1) % 4
            ro_cnt += 1
            now_len = 0
        if ro_cnt == 2:
            ro_cnt = 0
            max_len += 1
        x += dx[di]
        y += dy[di]
    return new_li


dxs = (-1, 1, 0, 0)
dys = (0, 0, -1, 1)
one, two, thr = 0, 0, 0
ans = 0
for _ in range(m):
    d, p = map(int, input().split())

    x, y = n // 2, n // 2
    for i in range(p):
        grid[x + dxs[d - 1]][y + dys[d - 1]] = 0
        x += dxs[d - 1]
        y += dys[d - 1]

    li = get_list()
    if len(li) == 0:
        break
    new_li = kill(li)
    if len(new_li) == 0:
        break
    tmp = kill(new_li)
    while new_li != tmp:
        new_li = tmp
        tmp = kill(new_li)

    re_list = remake(tmp)
    grid = fill(re_list)

    # print(ans)
    # print(li)
    # print(new_li)
    # print()

print(one + two * 2 + thr * 3)

for i in range(n):
    print(grid[i])
