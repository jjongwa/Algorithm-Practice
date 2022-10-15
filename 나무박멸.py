n, m, k, c = map(int, input().split())  # 격자 크기, 년수, 제초제 확산 범위, 제초제 남아있는 년수
grid = [list(map(int, input().split())) for _ in range(n)]
limit_sp = [[0 for _ in range(n)] for _ in range(n)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

ans = 0

def is_possible(x, y):
    return 0 <= x < n and 0 <= y <n

def grow(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                for d in range(4):
                    nx, ny = i + dx[d], j +dy[d]
                    if is_possible(nx, ny) and arr[nx][ny] > 0:
                        arr[i][j] += 1


def spread(arr):
    plus = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                spread_cnt = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if is_possible(nx, ny) and arr[nx][ny] == 0:
                        spread_cnt += 1
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if is_possible(nx, ny) and arr[nx][ny] == 0:
                        plus[nx][ny] += (arr[i][j] // spread_cnt)

    for i in range(n):
        for j in range(n):
            if plus[i][j] > 0:
                arr[i][j] += plus[i][j]


cx = (1, 1, -1, -1)
cy = (1, -1, 1, -1)


def kill(arr):
    global ans
    spray = [[0 for _ in range(n)] for _ in range(n)]
    kill_list = [[0 for _ in range(n)] for _ in range(n)]
    max_kill = [0, 0, 0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                kill_list[i][j] += arr[i][j]
                for d in range(4):
                    for kk in range(1, k+1):
                        nx, ny = i + cx[d]*kk, j + cy[d]*kk
                        if is_possible(nx, ny):
                            if arr[nx][ny] <=0:
                                break
                            elif is_possible(nx, ny) and arr[nx][ny] > 0:
                                kill_list[i][j] += arr[nx][ny]
                                if i == 3 and j == 2:
                                    print(arr[nx][ny])
                if max_kill[0] < kill_list[i][j]:
                    max_kill = [kill_list[i][j], i, j]

    ans += max_kill[0]
    print(max_kill)
    # print()
    #
    # for i in range(n):
    #     print(*kill_list[i])
    arr[max_kill[1]][max_kill[2]] = -2
    spray[max_kill[1]][max_kill[2]] = 1
    for d in range(4):
        for kk in range(1, k+1):
            nx, ny = max_kill[1] + cx[d]*kk, max_kill[2] + cy[d]*kk
            if is_possible(nx, ny):
                if arr[nx][ny] == -1:
                    break
                elif arr[nx][ny] == 0 or arr[nx][ny] == -2:
                    # arr[nx][ny] = -2
                    spray[nx][ny] = 1
                    break
                elif arr[nx][ny] > 0:
                    # arr[nx][ny] = -2
                    spray[nx][ny] = 1


    # for i in range(n):
    #     print(*arr[i])
    print("spray")
    for i in range(n):
        print(*spray[i])
    print()

    #제초제 시간 지남
    for i in range(n):
        for j in range(n):
            if limit_sp[i][j] > 0:
                limit_sp[i][j] += 1
                if limit_sp[i][j] == c+1:
                    limit_sp[i][j] = 0
                    arr[i][j] = 0
    # 새로운 제초제 시간 부여
    for i in range(n):
        for j in range(n):
            if spray[i][j] == 1:
                limit_sp[i][j] = 1
                arr[i][j] = -2

for mm in range(m):
    print("take ",mm)
    for i in range(n):
        print(*grid[i])

    grow(grid)
    spread(grid)
    print()
    for i in range(n):
        print(*grid[i])

    kill(grid)







    print()
    for i in range(n):
        print(*grid[i])

    print()
    for i in range(n):
        print(*limit_sp[i])

    print()
    print(ans)