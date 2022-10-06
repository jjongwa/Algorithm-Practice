import copy
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
# print(grid)

def is_possible(x, y):
    return 0 <= x < n and 0 <= y < m

def move(ar, d):
    arr = copy.deepcopy(ar)
    tri = 0
    if d == 0:  # 동
        for i in range(n):
            for j in range(m-1,-1,-1):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    if is_possible(i,j+1):
                        if arr[i][j+1] == '.':
                            arr[i][j+1] = arr[i][j]
                            arr[i][j] = '.'
                        elif arr[i][j+1] == 'O':
                            if arr[i][j] == 'R':
                                tri = 1
                            elif arr[i][j] == 'B':
                                tri = -1
    elif d == 1:   # 서
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    if is_possible(i,j-1):
                        if arr[i][j-1] == '.':
                            arr[i][j-1] = arr[i][j]
                            arr[i][j] = '.'
                        elif arr[i][j-1] == 'O':
                            if arr[i][j] == 'R':
                                tri = 1
                            elif arr[i][j] == 'B':
                                tri = -1
    elif d == 2:    #남
        for i in range(n-1,-1,-1):
            for j in range(m):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    if is_possible(i+1,j):
                        if arr[i+1][j] == '.':
                            arr[i+1][j] = arr[i][j]
                            arr[i][j] = '.'
                        elif arr[i+1][j] == 'O':
                            if arr[i][j] == 'R':
                                tri = 1
                            elif arr[i][j] == 'B':
                                tri = -1
    elif d == 3:    #북
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 'R' or arr[i][j] == 'B':
                    if is_possible(i-1,j):
                        if arr[i-1][j] == '.':
                            arr[i-1][j] = arr[i][j]
                            arr[i][j] = '.'
                        elif arr[i-1][j] == 'O':
                            if arr[i][j] == 'R':
                                tri = 1
                            elif arr[i][j] == 'B':
                                tri = -1
    return (tri, arr)


ansList = []
def bfs(arr, cnt):
    print(cnt)
    if cnt > 10:
        return
    for i in range(4):
        tmp = move(arr, i)
        print(tmp)
        if tmp[0] == 1:
            ansList.append(cnt)
            return
        elif tmp[0] == -1:
            continue
        else:
            bfs(tmp[1], cnt+1)

bfs(grid, 0)

print(ansList)