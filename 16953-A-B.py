from collections import deque

A, B = map(int, input().split())


def mul(num):
    return num * 2


def append(num):
    return num * 10 + 1


dq = deque()
dq.append([A, 1])

while dq:
    num, cnt = dq.popleft()
    # print(num, cnt)
    if num == B:
        print(cnt)
        exit(0)
        break
    elif num < B:
        dq.append([num * 2, cnt + 1])
        dq.append([num * 10 + 1, cnt + 1])
print(-1)
