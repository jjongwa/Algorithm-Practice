n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0 ,-1)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y< n

def art(arr):
    chk = [[0 for _ in range(n)] for _ in range(n)]
    many_list = {}
    # 구역 수 확인
    diff = [[0 for _ in range(n)] for _ in range(n)]
    diff_c = 0  # 구역 수
    for i in range(n):
        for j in range(n):
            stack = []
            if chk[i][j] == 0:
                chk[i][j] = 1
                diff[i][j] = diff_c
                stack.append([i, j])

                color = grid[i][j]
                many = 0
                while stack:
                    x, y = stack.pop()
                    many += 1
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if is_possible(nx, ny) and chk[nx][ny] == 0 and grid[nx][ny] == color:
                            chk[nx][ny] = 1
                            diff[nx][ny] = diff_c
                            stack.append([nx, ny])
                many_list[diff_c] = [grid[i][j], many]
                diff_c += 1

    # for i in range(n):
    #     print(*diff[i])
    # print()
    chk = [[0 for _ in range(n)] for _ in range(n)]
    cnt_s = [[0 for _ in range(n)] for _ in range(n)]
    nearList =[[0 for _ in range(diff_c)] for _ in range(diff_c)]

    # 구역당 사각형 개수
    for i in range(n):
        for j in range(n):
            stack = []
            if chk[i][j] == 0:
                chk[i][j] = 1
                stack.append([i, j])
                while stack:
                    x, y = stack.pop()
                    cnt_s[x][y] = many_list[diff[x][y]][1]
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if is_possible(nx, ny) and chk[nx][ny] == 0:
                            if diff[nx][ny] == diff[i][j]:
                                chk[nx][ny] = 1
                                stack.append([nx, ny])
                            else:
                                nearList[diff[i][j]][diff[nx][ny]] += 1
                                nearList[diff[nx][ny]][diff[i][j]] += 1
    # print()
    # for i in range(n):
    #     print(*cnt_s[i])
    # print()
    #
    # for i in range(diff_c):
    #     print(*nearList[i])
    # print()

    tmp = 0
    for i in range(diff_c):
        for j in range(diff_c):
            if i != j:
                # print(many_list[i][1], many_list[j][1],many_list[i][0],many_list[j][0],nearList[i][j])
                tmp += (many_list[i][1] + many_list[j][1])*many_list[i][0]*many_list[j][0]*nearList[i][j]
                # print()
    # print(tmp//2)
    # print()
    return tmp //2

def rotate_side(arr, s_x, s_y, s_l):
    new_g = [[0 for _ in range(s_l)] for _ in range(s_l)]
    # for _ in range(3):
    for i in range(s_l):
        for j in range(s_l):
            new_g[i][j] = arr[s_x+i][s_y+j]

    ro_g = zip(*new_g[::-1])
    ro_g = [list(e) for e in ro_g]
    for i in range(s_l):
        for j in range(s_l):
            arr[s_x+i][s_y+j] = ro_g[i][j]


def rotate_cross(arr):
    for _ in range(3):
        ro_g = zip(*arr[::-1])
        ro_g = [list(e) for e in ro_g]
        for i in range(n):
            arr[i][n//2] = ro_g[i][n//2]
            arr[n//2][i] = ro_g[n//2][i]

# art(grid)

ans = 0
for _ in range(3):
    ans += art(grid)

    # 십자 움직이기
    rotate_cross(grid)

    # 사각형 움직이기
    for i in range(2):
        for j in range(2):
            rotate_side(grid, i*(n//2+1), j*(n//2+1), n//2)

ans += art(grid)




print(ans)







    # print()
    # for i in range(n):
    #     print(*grid[i])
