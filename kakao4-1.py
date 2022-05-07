n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]      # 입구
summits = [5]    # 봉우리
answer = []

import copy
import heapq

way = [[]for _ in range(n+1)]
for i in paths:
    way[i[0]].append([i[1], i[2]])
    way[i[1]].append([i[0], i[2]])

#for i in way:
#    print(i)

INF = int(1e9)
distance = [INF] * (n+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0            # 시작노드->시작노드 거리 기록
    while q:
        node, dist = heapq.heappop(q)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[node] < dist:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in way[node]:
            cost = max(distance[node],next[1])   # 시작->node거리 + node->node의인접노드 거리
            if cost < distance[next[0]]:      # cost < 시작->node의인접노드 거리
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


for i in gates:
    dijkstra(i)


for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])




#ansList.sort(key=lambda x: (x[1], x[0]))


#answer = ansList[0]


#print(ansList)
print(answer)