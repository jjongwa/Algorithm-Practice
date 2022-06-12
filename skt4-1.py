grid = [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"]
k = 6

from collections import deque



dy = (0,1,0,-1)
dx = (1,0,-1,0)

answer = -1

check = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid[0]))] 

stack = []
stack.append((0,0,[grid[0][0]]))
ansList = []

while stack:
    x, y, trace = stack.pop()
    check[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and check[nx][ny] == 0:
            if nx == len(grid)-1 and ny == len(grid[0])-1:
                ansList.append(trace+list(grid[nx][ny]))
                check[x][y] = 0
            else:
                stack.append((nx,ny,trace+list(grid[nx][ny])))

print(ansList)


ansList2 = []
for i in range(len(ansList)):
    k_limit = 0
    dq = deque()
    dq.append((0, 0, 0))
    while True:
        tri = 0
        while dq:
            now, limit, cnt2 = dq.popleft()
            if now == len(ansList[i]) - 1:
                ansList2.append(cnt2)
                tri = 1
                break
            if now < limit:
                dq.append((now+1,limit+1, cnt2))
            if now <= k and cnt2 < k_limit:
                dq.append((now, 0, cnt2+1))
        if tri == 1:
            break
        k_limit += 1
print(ansList2)



