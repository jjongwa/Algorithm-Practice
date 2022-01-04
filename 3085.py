#   ªÁ≈¡ ∞‘¿”

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    board[i] = list(input())

def check(x, y):
    hei = []
    len = []

    tmp = 1
    for i in range(N-1):
        if board[i][y] == board[i+1][y]:
            tmp += 1
        else:
            hei.append(tmp)
            tmp = 1
        if i == N-1:
            hei.append(tmp)
        hei.append(tmp)

    tmp = 1
    for i in range(N-1):
        if board[x][i] == board[x][i+1]:
            tmp +=1
        else:
            len.append(tmp)
            tmp = 1
        if i == N-1:
            len.append(tmp)
        len.append(tmp)

    return max(max(len), max(hei))
 

#print(board)
ansList = []
for i in range(N-1):
    for j in range(N):
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        ansList.append(check(i,j))
        ansList.append(check(i+1,j))
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

for i in range(N):
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        ansList.append(check(i,j))
        ansList.append(check(i,j+1))
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]



print(ansList)
print(max(ansList))

