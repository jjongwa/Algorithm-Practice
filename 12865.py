N, K = map(int,input().split())
dpList = [[0 for _ in range(K+1)] for _ in range(N+1)]
#print(dpList)
thingList = []

for _ in range(N):
    W, V = map(int,input().split())
    thingList.append([W,V])


def knapsack(K, thingList):
    for i in range(len(thingList)):
        for j in range(K+1):
