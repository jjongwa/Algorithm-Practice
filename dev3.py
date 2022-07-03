from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

rows = 9
columns = 7
lands = [[2, 2], [2, 3], [2, 5], [3, 2], [3, 4], [3, 5], [3, 6], [4, 3], [4, 6], [5, 2], [5, 5], [6, 2], [6, 3], [6, 4], [6, 6], [7, 2], [7, 6], [8, 3], [8, 4], [8, 5]]

def solution(rows, columns, lands):
    
    fleid = [[0 for _ in range(columns)] for _ in range(rows)]
    for l in lands:
        fleid[l[0]-1][l[1]-1] = 1

    dq = deque()
    dq.append((0,0))
    fleid[0][0] = 2

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= x <= rows-1 and 0 <= y <= columns-1 and fleid[nx][ny] == 0:
                fleid[nx][ny] = 2
                dq.append((nx, ny))


    ansList = []

    

    for i in range(rows):
        for j in range(columns):
            if fleid[i][j] == 0:
                dq2 = deque()
                dq2.append((i,j))
                fleid[i][j] == 3
                cnt = 1
                while dq2:
                    x, y = dq2.popleft()
                    for i in range(4):
                        nx, ny = x+dx[i], y+dy[i]
                        if 0 <= x <= rows-1 and 0 <= y <= columns-1 and fleid[nx][ny] == 0:
                            fleid[nx][ny] = 3
                            dq2.append((nx, ny))
                            cnt += 1
                ansList.append(cnt)

    answer = fleid
    answer.append(ansList)
    return answer

print(solution(rows, columns, lands))