import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
grid = [input() for _ in range(N)]
chk = [[0 for _ in range(N)] for _ in range(N)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def is_possible(x,y):
    return 0 <= x < N and 0 <= y < N

stack=[]
cnt = 0
for i in range(N):
    for j in range(N):
        if chk[i][j] == 0:
            stack.append((i,j))
            chk[i][j] =1
            cnt += 1
            while stack:
                x, y = stack.pop()
                color = grid[x][y]
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if is_possible(nx,ny) and chk[nx][ny] == 0 and grid[nx][ny] == color:
                        chk[nx][ny] = 1
                        stack.append((nx,ny))

print(cnt, end=' ')     
chk = [[0 for _ in range(N)] for _ in range(N)]
stack=[]
cnt = 0
for i in range(N):
    for j in range(N):
        if chk[i][j] == 0:
            stack.append((i,j))
            chk[i][j] =1
            cnt += 1
            while stack:
                x, y = stack.pop()
                color = grid[x][y]
                if color == 'G' or color == 'R':
                    tri = 1
                else:
                    tri = 0
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if tri:
                        if is_possible(nx,ny) and chk[nx][ny] == 0 and (grid[nx][ny] == 'G' or grid[nx][ny] == 'R'):
                            chk[nx][ny] = 1
                            stack.append((nx,ny))
                    else:
                        if is_possible(nx,ny) and chk[nx][ny] == 0 and grid[nx][ny] == color:
                            chk[nx][ny] = 1
                            stack.append((nx,ny))            
print(cnt)

