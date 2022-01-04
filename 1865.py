TC = int(input())
for tc in range(TC):
    N, M, W = map(int,input().split())
    way = [[] for _ in range(N+1)]
    
    
    for m in range(M):
        S, E, T = map(int,input().split())
        way[S].append([E,T])
        way[E].append([S,T])
    for w in range(W):
        S, E, T = map(int,input().split())
        way[S].append([E,-T])      
    
    #print(way)
    ansList = []
    def travel(start, now, time):
        for i in range(len(way[now])):
            if start == way[now][i][0]:
                ansList.append(time+way[now][i][1])
            else:
                travel(start, way[now][i][0],time+ way[now][i][1])

    for i in range(1,N+1,1):
        travel(i,i,0)

    print(ansList)