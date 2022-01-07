N, K = map(int,input().split())
dpList = [[0 for _ in range(K+1)] for _ in range(N+1)]
#print(dpList)
thingList = []

for _ in range(N):
    W, V = map(int,input().split())
    thingList.append([W,V])


def knapsack(K, thingList):
    for i in range(len(thingList)+1):
        for j in range(K+1):
            if i == 0 or j == 0:
                dpList[i][j] = 0
            elif thingList[i-1][0] <= j:
                dpList[i][j] = max(thingList[i-1][1]+dpList[i-1][j-thingList[i-1][0]],dpList[i-1][j])
            else:
                dpList[i][j] = dpList[i-1][j]

knapsack(K,thingList)

print(dpList[N][K])