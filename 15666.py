#   N°ú M(12)
#   N°ú M (10)
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
    for i in range(x,N):
      
        stack.append(i)
        solve(i)
        stack.pop()

solve(0)
for i in ansList:
    print(' '.join(map(str,i)))
