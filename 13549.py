from collections import deque

N, K = map(int, input().split())

q = deque([N])
time = [-1] * 100001
time[N] = 0

def bfs():
    while q:
        start = q.popleft()
        if start == K:
            return time[start]
        for i in range(3):
            if i ==0:
                tmp = start + 1
            elif i == 1: 
                tmp = start - 1
            else:
                tmp = start*2

            if not 0 <= tmp < 100001:
                continue
            elif time[tmp] != -1 and time[tmp] <= time[start]:
                continue

            if i <2:
                q.append(tmp)
                time[tmp] = time[start] + 1
            else:
                q.appendleft(tmp)
                time[tmp] = time[start]

print(bfs())           


# dijkstra  or  BFS