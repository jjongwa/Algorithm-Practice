import heapq

hq = []
cnt = 0
N = int(input())
for _ in range(N):
    heapq.heappush(hq, int(input()))
print(hq)
while len(hq) > 1:
    new_num = heapq.heappop(hq) + heapq.heappop(hq)
    cnt += new_num
    heapq.heappush(hq, new_num)


# print(hq)
print(cnt)
