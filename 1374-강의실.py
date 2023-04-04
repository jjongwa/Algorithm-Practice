import heapq

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort(key=lambda x: x[1])

minHeap = []
ans = 0

for c in classes:
    while minHeap and minHeap[0] <= c[1]:
        heapq.heappop(minHeap)
    heapq.heappush(minHeap, c[2])
    ans = max(ans, len(minHeap))

print(ans)

