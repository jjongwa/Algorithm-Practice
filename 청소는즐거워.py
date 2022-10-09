n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def is_possible(x,y):
    return 0 <= x < n and 0 <= y < n

def clean(x, y, d):
    global ans
    if d == 0:
        left = grid[x][y]
        if is_possible(x,y-2):
            grid[x][y-2] += ((grid[x][y] * 5) // 100)
        else:
            ans += ((grid[x][y] * 5) // 100)
        left -= ((grid[x][y] * 5) // 100)

        if is_possible(x-1,y):
            grid[x-1][y] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)
        if is_possible(x+1,y):
            grid[x+1][y] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)

        if is_possible(x-1,y-1):
            grid[x-1][y-1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        if is_possible(x+1,y-1):
            grid[x+1][y-1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        
        if is_possible(x-1,y+1):
            grid[x-1][y+1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)
        if is_possible(x+1,y+1):
            grid[x+1][y+1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)

        if is_possible(x-2,y):
            grid[x-2][y] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)
        if is_possible(x+2,y):
            grid[x+2][y] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)

        if is_possible(x,y-1):
            grid[x][y-1] += left
        else:
            ans += left

    if d == 1: #아래
        left = grid[x][y]
        if is_possible(x+2,y):
            grid[x+2][y] += ((grid[x][y] * 5) // 100)
        else:
            ans += ((grid[x][y] * 5) // 100)
        left -= ((grid[x][y] * 5) // 100)

        if is_possible(x,y-1):
            grid[x][y-1] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)
        if is_possible(x,y+1):
            grid[x][y+1] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)

        if is_possible(x+1,y-1):
            grid[x+1][y-1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        if is_possible(x+1,y+1):
            grid[x+1][y+1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        
        if is_possible(x-1,y-1):
            grid[x-1][y-1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)
        if is_possible(x-1,y+1):
            grid[x-1][y+1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)

        if is_possible(x,y-2):
            grid[x][y-2] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)
        if is_possible(x,y+2):
            grid[x][y+2] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)

        if is_possible(x+1,y):
            grid[x+1][y] += left
        else:
            ans += left




    if d == 2: #오른쪽
        left = grid[x][y]
        if is_possible(x,y+2):
            grid[x][y+2] += ((grid[x][y] * 5) // 100)
        else:
            ans += ((grid[x][y] * 5) // 100)
        left -= ((grid[x][y] * 5) // 100)

        if is_possible(x-1,y):
            grid[x-1][y] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)
        if is_possible(x+1,y):
            grid[x+1][y] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)

        if is_possible(x-1,y+1):
            grid[x-1][y+1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        if is_possible(x+1,y+1):
            grid[x+1][y+1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        
        if is_possible(x-1,y-1):
            grid[x-1][y-1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)
        if is_possible(x+1,y-1):
            grid[x+1][y-1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)

        if is_possible(x-2,y):
            grid[x-2][y] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)
        if is_possible(x+2,y):
            grid[x+2][y] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)

        if is_possible(x,y+1):
            grid[x][y+1] += left
        else:
            ans += left


    if d == 3: #위
        left = grid[x][y]
        if is_possible(x-2,y):
            grid[x-2][y] += ((grid[x][y] * 5) // 100)
        else:
            ans += ((grid[x][y] * 5) // 100)
        left -= ((grid[x][y] * 5) // 100)

        if is_possible(x,y-1):
            grid[x][y-1] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)
        if is_possible(x,y+1):
            grid[x][y+1] += ((grid[x][y] * 7) // 100)
        else:
            ans += ((grid[x][y] * 7) // 100)
        left -= ((grid[x][y] * 7) // 100)

        if is_possible(x-1,y-1):
            grid[x-1][y-1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        if is_possible(x-1,y+1):
            grid[x-1][y+1] += ((grid[x][y] * 10) // 100)
        else:
            ans += ((grid[x][y] * 10) // 100)
        left -= ((grid[x][y] * 10) // 100)
        
        if is_possible(x+1,y-1):
            grid[x+1][y-1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)
        if is_possible(x+1,y+1):
            grid[x+1][y+1] += (grid[x][y] // 100)
        else:
            ans += (grid[x][y] // 100)
        left -= (grid[x][y] // 100)

        if is_possible(x,y-2):
            grid[x][y-2] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)
        if is_possible(x,y+2):
            grid[x][y+2] += ((grid[x][y]*2) // 100)
        else:
            ans += ((grid[x][y]*2) // 100)
        left -= ((grid[x][y]*2) // 100)

        if is_possible(x-1,y):
            grid[x-1][y] += left
        else:
            ans += left

    grid[x][y] = 0

# for i in range(n):
#     print(*grid[i])
# print()


x, y = n//2, n//2-1
n_l = 0
m_l = 1
attemp = 0
direction = 0

# clean(n//2, n//2-1, 0)

while True:
    # print("x:",x," y:", y," direction:", direction," n_l:", n_l," m_l:", m_l," attemp:", attemp)
    clean(x, y, direction)
    n_l += 1
    if n_l == m_l:
        direction += 1
        n_l = 0
        attemp += 1
        if attemp == 2:
            attemp = 0
            m_l += 1
    if direction == 4:
        direction = 0

    if x == 0 and y == 0:
        break



    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x -= 1


    # for i in range(n):
    #     print(*grid[i])
    # print()


print(ans)