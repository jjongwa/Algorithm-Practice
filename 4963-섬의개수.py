import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10**6)
dy = (0,1,0,-1,1,1,-1,-1)
dx = (1,0,-1,0,-1,1,-1,1)

def dfs(x,y, arr, chk):
    global w, h
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1 and chk[nx][ny] == 0:
            chk[nx][ny] = 1
            dfs(nx, ny, arr, chk)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    m = []
    chk = [[0 for _ in range(w)] for _ in range(h)]
    ans = 0
    for _ in range(h):
        m.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if chk[i][j] == 0 and m[i][j] == 1:
                ans += 1
                dfs(i,j, m, chk)
    print(ans)