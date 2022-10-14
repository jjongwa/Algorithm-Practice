from collections import deque
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
f = [[0 for _ in range(n)] for _ in range(n)]
walls = []  # 벽 위치
office = [] # 사무실 위치
dx = (0,-1,0,1)
dy = (-1,0,1,0)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            office.append([i, j])


def is_possible(cx, cy):
    return 0 <= cx < n and 0 <= cy < n

def turn(x, y, d):
    dq = deque()
    if d == 2:
        return
    elif d == 3:
        return
    elif d == 4:
        dq.append([x, y+1, 5])

        while dq:


        for j in range(1, 6):
            for i in range(-j+1, j):
                if is_possible(x+i, y+j):
                    if [x+i, y+j, 1] not in walls:
                        f[x+i][y+j] += (6-j)
    elif d == 5:
        return



for _ in range(m):  # 벽에 대한 정보
    x, y, s = map(int, input().split())
    walls.append([x, y, s])
print(walls)

turn(1,0,4)

print()
for i in range(n):
    print(*f[i])
print()
for i in range(n):
    print(*grid[i])
