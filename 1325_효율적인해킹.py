N, M = map(int, input().split())
com = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    com[B].append(A)
#print(com)
visited = [0 for _ in range(N+1)]

def dfs(start):
    #print(visited)
    stack = []
    stack.append(start)
    while stack:
        tmp = stack.pop()
        if visited[tmp] == 1:
            continue
        visited[tmp] = 1
        #print(com[tmp])  
        stack.extend(com[tmp])
        #print(stack)

    return sum(visited)


ansList = [0 for _ in range(N+1)]
for i in range(1, N+1):
    ansList[i] += dfs(i)
    visited = [0 for _ in range(N+1)]

#print(ansList)

m = max(ansList)
ans = [i for i, v in enumerate(ansList) if v == m]
# m을 max값으로 놓고 enumerate를 이용해 i(index), v(값)을 구해 i만 뽑아낸다

for i in ans:
    print(i, end=' ')


# pypy 통과 -> 시간 줄일 방법을 찾아보자 -> 재귀형식으로 바꿔보자