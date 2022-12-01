n, m = map(int, input().split())

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < m

grid = [[0 for _ in range(m)] for _ in range(n)]

st = 1
x, y, dirt = 0, 0, 1
while True:
    if dirt == 1: #상승
        while is_possible(x,y):
            grid[x][y] = st
            st += 1
            if is_possible(x-1,y+1):
                x -= 1
                y += 1
            else:
                break
        if is_possible(x, y+1):
            y += 1
            dirt = 0
        elif is_possible(x+1, y) and grid[x+1][y] == 0:
            x += 1
            dirt = 0
        else:
            break
    else: #하강
        while is_possible(x,y):
            grid[x][y] = st
            st += 1
            if is_possible(x+1,y-1):
                x += 1
                y -= 1
            else:
                break
        if is_possible(x+1, y):
            x += 1
            dirt = 1
        elif is_possible(x, y+1) and grid[x][y+1] == 0:
            y += 1
            dirt = 1
        else:
            break

for i in range(n):
    print(*grid[i])