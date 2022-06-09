import sys
sys.stdin = open('input.txt', 'r')

numList = [0 for _ in range(10)]

A = int(input())
B = int(input())
C = int(input())

ans = A*B*C

for n in str(ans):
    numList[int(n)] += 1

for a in numList:
    print(a)