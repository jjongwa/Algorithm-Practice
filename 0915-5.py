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

n, m  = map(int, input().split())
coinList = list(map(int, input().split()))

dq = deque()
dq.append([0,0])

while dq:
    now, nowsum  = dq.popleft()
    for c in coinList:
        nxtsum = nowsum + c
        if nxtsum == m:
            print(now+1)
            exit(0)
        else:
            dq.append([c, nxtsum])

    
