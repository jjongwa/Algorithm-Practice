grid = [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"]
k = 6

from collections import deque



dy = (0,1,0,-1)
dx = (1,0,-1,0)
dq = deque()

answer = -1

check = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid[0]))] 

k_limit = 0
while True:
    dq.append((0,0,0,0))    # x, y, cnt, k
    while dq:
        x, y, cnt, mov = dq.pop()
        check[x][y] = 1
        tri = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and check[nx][ny] == 0 and mov <k:
                if nx == len(grid)-1 and ny == len(grid[0])-1:
                    answer = cnt
                    tri = 1
                    break
                dq.append((nx,ny,cnt,mov+1))
                
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and mov <=k and grid[x][y] == "." and cnt < k_limit:
                dq.append((x,y,cnt+1,0))
        if tri == 1:
            break
        
        

    if answer != -1:
        break
    k_limit += 1
    
print(answer)
        
    

