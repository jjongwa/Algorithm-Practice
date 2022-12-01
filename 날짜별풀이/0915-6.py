n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1]
dy = [1,0]

ansList =[]

def is_possible(x,y):
    return 0 <= x < n and 0 <= y < n

def dfs(path, x, y):
    if x == n-1 and y == n-1:
        path.sort()
        ansList.append(path[k-1])
        return
    
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if is_possible(nx,ny):
            
            path.append(grid[nx][ny])
            dfs(path,nx,ny)

dfs([grid[0][0]],0,0)
print(ansList)
print(min(ansList))