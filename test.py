from collections import deque
dy = (0,1,0,-1)
dx = (1,0,-1,0)
chk = [[False] * 100 for _ in range(100)]
N = int(input())

def is_valid_coord(y,x):            # 좌표가 범위를 벗어나지 않는지
    return 0 <= y < N and 0 <=x <N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y,start_x))
    while len(q) > 0:
        y, x = q.popleft()
        chk[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny,nx) and not chk[ny][nx]:
                q.append((ny,nx))



SELECT C1.NAME NAME_X, C2.NAME NAME_Y, count(C1.CART_ID) "장바구니 수"
from CART_PRODUCTS C1
join CART_PRODUCTS C2 on C1.CART_ID = C2.CART_ID
group by C1.CART_ID

-- 코드를 입력하세요
SELECT C1.NAME NAME_X, C2.NAME NAME_Y, count(C1.CART_ID) "장바구니 수"
from (select distinct C.CART_ID, distinct C.NAME
      from CART_PRODUCTS C) C1
join (select distinct C.CART_ID, distinct C.NAME
      from CART_PRODUCTS C)C2 on C1.CART_ID = C2.CART_ID and C1.Name != C2.Name
group by C1.CART_ID



SELECT C1.NAME NAME_X, C2.NAME NAME_Y, count(C1.CART_ID) "장바구니 수"
from (select distinct C.CART_ID, C.NAME
      from CART_PRODUCTS C) C1
join (select distinct C.CART_ID, C.NAME
      from CART_PRODUCTS C)C2 on C1.CART_ID = C2.CART_ID and C1.Name != C2.Name
group by C1.CART_ID
order by C1.name, C2.name

'''
# BFS
from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1
adj[3][7] = adj[3][8] = 1
adj[4][9] = 1
adj[2][5] = adj[2][6] = 1

def bfs():
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        print(now, end=' ')
        for nxt in range(13):
            if adj[now][nxt]:   # 엣지가 있으면
                dq.append(nxt)  # 큐에 넣어준다

bfs()
'''


'''
# DFS
adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1
adj[5][6] = 1

def dfs(now):               #시작점이 now인 엣지 탐색
    print(now, end=' ')
    for nxt in range(13):   
        if adj[now][nxt]:   # [now][nxt] = 1이면
            dfs(nxt)        # nxt가 시작점인 엣지 탐색

dfs(0)
'''