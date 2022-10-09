from collections import deque
n, k = map(int, input().split())
walk = deque(list(map(int, input().split())))
man = deque([0] * (n*2))

def mov(arr):
    tmp  = arr[2*n-1]
    arr.appendleft(tmp)
    arr.pop()


act = 0
cnt = 0
while True:
    act += 1
    # 무빙워크가 한 칸 회전합니다.
    mov(walk)
    mov(man)
    if man[n-1] == 1:
        man[n-1] = 0  # 하차
    # 무빙워크가 회전하는 방향으로 이동
    for i in range(n-1, 0, -1):
        if man[i] == 1 and man[i+1] == 0 and walk[i+1] > 0:
            man[i+1] = 1
            man[i] = 0
            walk[i+1] -= 1
            if walk[i+1] == 0:
                cnt += 1
    if man[n-1] == 1:
        man[n-1] = 0  # 하차

    # 사람 올리기
    if walk[0] != 0:
        # act += 1
        man[0] = 1
        walk[0] -= 1
        if walk[0] == 0:
            cnt += 1

    if cnt >= k:
        print(act)
        break

    print(walk)
    print(man)
    print(act)
    print()

print(walk)
print(man)