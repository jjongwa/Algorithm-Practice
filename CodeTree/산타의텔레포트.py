from collections import deque


def is_possible(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
chk = [[0 for _ in range(m)] for _ in range(n)]

