import sys
import heapq
input = sys.stdin.readline
N = int(input())
pq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heapq.heappop(pq)[1] if pq else 0)
    else:
        heapq.heappush(pq, (abs(x), x))