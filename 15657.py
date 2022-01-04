#   N°ú M (8)
N, M = map(int, input().split())
numList = list(map(int,input().split()))
numList.sort()
stack = []
def solve(x):
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    for i in range(x,len(numList)):
        stack.append(numList[i])
        solve(i)
        stack.pop()

solve(0)
