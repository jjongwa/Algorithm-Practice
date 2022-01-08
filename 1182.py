from itertools import combinations
N, S = map(int, input().split())
numList = list(map(int,input().split()))
#print(numList)
ans = 0
for i in range(N):
    combi = combinations(numList, i+1)
    for j in combi:
        if sum(j) == S:
            ans+=1
            #print(i, j)
print(ans)