from collections import deque


def magic(dq, n):
    dq.appendleft(n)
    for _ in range(n):
        k = dq.pop()
        dq.appendleft(k)


N = int(input())
dq = deque([N])
for i in range(N - 1, 0, -1):
    magic(dq, i)

print(*dq)
