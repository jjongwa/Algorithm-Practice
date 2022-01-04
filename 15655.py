#   N°ú M (6)
N, M = map(int, input().split())
numList = list(map(int,input().split()))
numList.sort()
stack = []
def solve(x):
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    for i in range(x,len(numList)):
        if numList[i] in stack:
            continue
        stack.append(numList[i])
        solve(i+1)
        stack.pop()

solve(0)