N, K = map(int,input().split())
thingList = []
for _ in range(N):
    W, V = map(int,input().split())
    thingList.append([W,V])


def knapsack(capacity, n):
    if capacity == 0 or n == 0:
        return 0
    if size[n-1] > capasity:
        return knapsack(capacity, n-1)
    else:
        return max()