import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
input=sys.stdin.readline
R, C = map(int, input().split())
board = [input() for _ in range(R)]
chk = set()

dy = (0,1,0,-1)
dx = (1,0,-1,0)

def is_possible(x, y):
    return 0 <= x < R and 0 <= y < C

count = 1
def dfs(x, y, cnt):
    global count
    count = max(cnt, count)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if is_possible(nx,ny) and board[nx][ny] not in chk:
            chk.add(board[nx][ny])
            dfs(nx,ny,cnt+1)          
            chk.remove(board[nx][ny])
    
chk.add(board[0][0])
dfs(0,0,1)
print(count)