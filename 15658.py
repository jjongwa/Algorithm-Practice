N = int(input())
numList = list(map(int, input().split()))
operators = list(map(int, input().split()))

ansmax = -1e9
ansmin = 1e9

def DFS(now, ans, plus, minus, mul, div):
    global ansmax, ansmin
    if now == N:
        ansmax = max(ans, ansmax)
        ansmin = min(ans, ansmin)
        return

    if plus:
        DFS(now+1, ans+ numList[now], plus-1, minus, mul, div)
    if minus:
        DFS(now+1, ans- numList[now], plus, minus-1, mul, div)
    if mul:
        DFS(now+1, ans* numList[now], plus, minus, mul-1, div)
    if div:
        DFS(now+1, int(ans/ numList[now]), plus, minus, mul, div-1)

DFS(1,numList[0], operators[0], operators[1], operators[2], operators[3])

print(ansmax)
print(ansmin)


