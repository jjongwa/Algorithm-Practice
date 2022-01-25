N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(input()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0

# dfs
def dfs(start_x, start_y, now_x,now_y, cnt, color):
    global ans
    if ans == 1:
        return
    
    visited[now_x][now_y] = 1

    if start_x == now_x and start_y == now_y and cnt >=4:
        ans = 1
        return

    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and color == field[nx][ny]:
                dfs(start_x,start_y, nx, ny, cnt+1, color)
            elif nx == start_x and ny == start_y and cnt >=4:
                dfs(start_x, start_y, nx, ny, cnt, color)

    return

for i in range(N):
    for j in range(M):
        visited = [[0]*M for _ in range(N)]
        visited[i][j] = 1
        dfs(i,j,i,j,1,field[i][j])

if ans:
    print("Yes")
else:
    print("No")



'''
def cycle(st_r, st_c, now_r, now_c, step):
    if step == 1:
        if field[now_r][now_c] == field[now_r][now_c+1]:
            cycle(st_r,st_c, now_r, now_c+1, 1)
        elif st_r == now_r and st_c == now_c:
            return 0
        else:
            cycle(st_r,st_c, now_r, now_c, 2)
    elif step == 2:
        if field[now_r][now_c] == field[now_r+1][now_c]:
            cycle(st_r,st_c, now_r+1, now_c, 2)
        elif st_r == now_r and st_c == now_c:
            return 0
        else:
            cycle(st_r,st_c, now_r, now_c, 3)
    elif step == 3:
        if field[now_r][now_c] == field[now_r][now_c-1]:
            cycle(st_r,st_c, now_r, now_c-1, 3)
        elif st_r == now_r and st_c == now_c:
            return 0
        else:
            cycle(st_r,st_c, now_r, now_c, 4)
    elif step == 4:
        if field[now_r][now_c] == field[now_r-1][now_c]:
            cycle(st_r,st_c, now_r-1, now_c, 4)
        elif st_r == now_r and st_c == now_c:
            return 1
        else:
            cycle(st_r,st_c, now_r, now_c, 4)
ans = 0
for i in range(N):
    for j in range(M):
        ans = cycle(i,j,i,j,1)
        if ans == 1:
            print("Yes")
            break

    
'''