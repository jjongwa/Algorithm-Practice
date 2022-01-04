INF = float('inf')

TC = int(input())
for tc in range(TC):
    N, M, W = map(int,input().split())
    way = []
    
    for m in range(M):
        S, E, T = map(int,input().split())
        way.append([S,E,T])
        way.append([E,S,T])
    for w in range(W):
        S, E, T = map(int,input().split())
        way.append([S,E,-T])    

    def travel(start):
        dist = [5000 * 10000] * (N+1)
        dist[start] = 0
        for i in range(N):
            for s,e,t in way:
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
                    if i == N-1:
                        return -1
        return 1
    ans = 0
    
    if travel(1) == -1:
        print('YES')
        ans = 1
        
    if ans == 0:
        print('NO')

        
    #hint:  Bellman-Ford Algorithm