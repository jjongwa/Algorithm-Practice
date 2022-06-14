import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
N = int(input())
for _ in range(N):
    N, M = map(int, input().split())
    dq = deque(map(int, input().split()))
    target = dq[M]
    cnt = 1
    while True:
        if dq[0] >= max(dq):
            if M == 0:
                print(cnt)
                break
            dq.popleft()
            M -= 1
            cnt += 1
        else:
            if M == 0:
                M = len(dq)-1
            else:
                M -= 1
            tmp = dq.popleft()
            dq.append(tmp)
            
            