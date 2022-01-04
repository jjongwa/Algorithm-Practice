#   N°ú M (9)
N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != L[i]:
            visited[i] = True
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)














'''
N, M = map(int, input().split())
numList = list(map(int,input().split()))
numList.sort()
stack = []
ansList = []
def solve(x):
    if len(stack) == M:
        tmp = [numList[x] for x in stack]
        if tmp not in ansList:
            ansList.append(tmp)
        return
    for i in range(N):
        if i in stack:
            continue
        stack.append(i)
        solve(i+1)
        stack.pop()

solve(0)
for i in ansList:
    print(' '.join(map(str,i)))
'''
