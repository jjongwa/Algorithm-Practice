import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]  # list() 를 안해줘서 시초가 났었다 레전드
chk = set()

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

print(board)


def is_possible(x, y):
    return 0 <= x < R and 0 <= y < C


count = 1


def dfs(x, y, cnt):
    global count
    count = max(cnt, count)
    chk.add(board[x][y])
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if is_possible(nx, ny) and board[nx][ny] not in chk:
            dfs(nx, ny, cnt + 1)
    chk.remove(board[x][y])


# chk.add(board[0][0])
dfs(0, 0, 1)
print(count)
