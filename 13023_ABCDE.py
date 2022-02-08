#   ABCDE
N, M = map(int,input().split())
camp = [ [] for _ in range(N)]
#print(camp)
for _ in range(M):
    a, b = map(int,input().split())
    camp[a].append(b)
    camp[b].append(a)
#print(camp)

visited = [0] * N

def dfs(start,level):
    if level == 5:
        print(1)
        exit()
    for i in camp[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, level+1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(i,1)
    visited[i] = False

print(0)