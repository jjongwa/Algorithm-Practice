# DFS
N = int(input())
num = list(map(int,input().split()))
operators = list(map(int,input().split()))

ansmax = -1e9
ansmin = 1e9

def DFS(depth, tmp, plus, minus, multiply, divide):
    global ansmax, ansmin
    if depth == N:
        ansmax = max(tmp, ansmax)
        ansmin = min(tmp, ansmin)
        return
    if plus:
        DFS(depth+1, tmp+num[depth], plus-1, minus, multiply, divide)
    if minus:
        DFS(depth+1, tmp-num[depth], plus, minus-1, multiply, divide)
    if multiply:
        DFS(depth+1, tmp*num[depth], plus, minus, multiply-1, divide)
    if divide:
        DFS(depth+1, int(tmp/num[depth]), plus, minus, multiply, divide-1)

DFS(1, num[0], operators[0], operators[1], operators[2], operators[3])
print(ansmax)
print(ansmin)