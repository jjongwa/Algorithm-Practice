'''
n, m  = map(int, input().split())
coinList = list(map(int, input().split()))
coinList.sort()

tmp = []
def Choose(cnt, limit):
    # 종료조건
    if cnt == limit+1:
        if sum(tmp) == m:
            pick.append(sum(tmp))
        return

    # 재귀호출 1~k
    for i in coinList:
        tmp.append(i)
        Choose(cnt+1, limit)
        tmp.pop()


for i in range(1,10001):
    pick = []    
    Choose(1,i)
    for p in pick:
        if p == m:
            print(i)
            exit(0)

print(-1)
'''

# 방향성이 없는 문제는 dp로 풀리지 않는다

from collections import deque
import sys
MAX_INT = sys.maxsize
n, m  = map(int, input().split())
coins = list(map(int, input().split()))

cnt = [MAX_INT]*(m+1)
chk = [0] *(m+1)

dq = deque()
dq.append([0,0])
chk[0] = 1

while dq:
    nowcnt, nowsum  = dq.popleft()
    
    for c in coins:
        nxt_sum = nowsum + c
        if 0 <= nxt_sum <= m and chk[nxt_sum] == 0:
            cnt[nxt_sum] = nowcnt+1
            chk[nxt_sum] = 1
            dq.append([nowcnt+1, nxt_sum])

if cnt[m] == MAX_INT:
    print(-1)
else:
    print(cnt[m])
    