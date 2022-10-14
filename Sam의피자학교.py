from collections import deque

n, k = map(int, input().split())
dow = deque(map(int, input().split()))


def put_flow():
    min_d = min(dow)
    for i in range(len(dow)):
        if dow[i] == min_d:
            dow[i] += 1


def roll(arr):
    dq = deque()
    dq.append(deque([arr.popleft()]))
    dq.append(arr)

    # print(dq)
    while len(dq) <= len(dq[len(dq)-1]) - len(dq)+1:
        new_dq = deque()
        for i in range(len(dq[0])):
            tmp = []
            for j in range(len(dq)-1, -1, -1):
                # print(j, i)
                tmp.append(dq[j][i])
            new_dq.append(deque(tmp))
            # print(tmp)
        tmp2 = deque(dq[len(dq)-1])
        # print(tmp2)
        for _ in range(len(dq[0])):
            tmp2.popleft()
        # new_dq.append(deque(tmp))
        new_dq.append(tmp2)

        dq = new_dq
        # print(dq)
        # print()
    return dq


dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def dow_push(arr):
    new_grid = [[0 for _ in range(len(arr[len(arr)-1]))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # print(i, j, arr[i][j])
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[nx]):
                    # print(nx, ny)
                    # print()
                    diff = abs(arr[i][j] - arr[nx][ny]) // 5

                    if diff > 0:
                        # print([i, j, arr[i][j]], [nx, ny, arr[nx][ny]], diff)
                        if arr[i][j] > arr[nx][ny]:
                            new_grid[i][j] -= diff
                            new_grid[nx][ny] += diff
                        else:
                            new_grid[i][j] += diff
                            new_grid[nx][ny] -= diff
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_grid[i][j] = new_grid[i][j] // 2 + arr[i][j]

    # print(new_grid)

    new_dow = []
    for j in range(len(new_grid[0])):
        tmp = []
        for i in range(len(new_grid)-1,-1,-1):
            if new_grid[i][j] != 0:
                tmp.append(new_grid[i][j])
        new_dow += tmp

    return deque(new_dow)


def fold(arr):
    tmp = deque()
    for _ in range(len(arr)//2):
        tmp.appendleft(arr.popleft())
    first_dow = deque([tmp, arr])
    # print(first_dow)
    second_dow = deque()
    first_len =len(first_dow[0])//2
    for i in range(2):
        tmp = deque()
        for j in range(first_len):
            tmp.appendleft(first_dow[i].popleft())
        second_dow.appendleft(tmp)
    second_dow += first_dow
    return second_dow

cnt = 0
while True:
    cnt += 1
    put_flow()
    print(dow)
    dow = roll(dow)
    print(dow)
    dow = dow_push(dow)
    print(dow)
    dow = fold(dow)
    print(dow)
    dow = dow_push(dow)
    print(dow)
    if max(dow) - min(dow) <= k:
        print(cnt)
        break
# rotate([2,10], 2, 1)

    print()



