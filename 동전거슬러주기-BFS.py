import sys
from collections import deque
MAX_INT = sys.maxsize
n, m  = map(int, input().split())
coins = list(map(int, input().split()))

cnt = [MAX_INT]*(m+1)
chk = [0]*(m+1)
dq = deque()

dq.append([0,0])
chk[0] = 1
while dq:
    n_cnt, n_sum = dq.popleft()

    if n_sum == m:
        continue
    for i in range(n):
        nxt_sum = n_sum + coins[i] 
        if nxt_sum <= m and chk[nxt_sum] == 0:
            cnt[nxt_sum] = min(cnt[nxt_sum], n_cnt+1)
            dq.append([n_cnt+1, nxt_sum])
            chk[nxt_sum] = 1

if cnt[m] == MAX_INT:
    print(-1)
else:
    print(cnt[m])