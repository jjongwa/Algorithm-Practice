from collections import deque
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = (0,1,1)
dy = (1,0,1)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n

dq = deque([[0, 1, 0, 1]])  # 가로 0 세로 1 대각 2

if grid[n-1][n-1] == 1:
    print(0)
    exit(0)
cnt = 0
chk = [[0 for _ in range(n)] for _ in range(n)]
while dq:
    x, y, d, c = dq.popleft()

    for i in range(3):
        if d == 0 and i == 1:
            continue
        if d == 1 and i == 0:
            continue
        nx, ny = x + dx[i], y + dy[i]
        if i == 0 or i == 1:
            if is_possible(nx, ny) and grid[nx][ny] == 0:
                if nx == n-1 and ny == n-1:
                    cnt += 1
                else:
                    dq.append([nx, ny, i])
        elif i == 2:
            if is_possible(nx, ny) and grid[nx][ny] == 0 and grid[nx-1][ny] == 0 and grid[nx][ny-1] == 0:
                if nx == n-1 and ny == n-1:
                    cnt += 1
                else:
                    dq.append([nx, ny, i])

print(cnt)