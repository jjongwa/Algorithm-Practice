import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
numList = list(map(int, input().split()))

sumList = [0 for _ in range(N+1)]
for i in range(1,len(numList)+1):
    sumList[i] = sumList[i-1] + numList[i-1]

for _ in range(M):
    s, e  = map(int, input().split())
    print(sumList[e]-sumList[s-1])
