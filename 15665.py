#   N°ú M(11)
N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if overlap != L[i]:
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            out.pop()

solve(0, N, M)



'''
N, M = map(int, input().split())
numList = list(map(int,input().split()))
numList.sort()
stack = []
ansList =[]
def solve():
    if len(stack) == M:
        tmp = [x for x in stack]
        if tmp not in ansList:
            ansList.append(tmp)
        return
    for i in numList:
        stack.append(i)
        solve()
        stack.pop()

solve()

for i in ansList:
    print(' '.join(map(str,i)))
'''

