from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
statList = {}
title = []
power = [-1]
for _ in range(N):
    a, b = input().split()
    title.append(a)
    power.append(int(b))
    statList[a] = int(b)



for _ in range(M):
    p = int(input())
    index = bisect_left(power, p)
    #print(index)
    print(title[index - 1])

'''
cha = [int(input().rstrip()) for _ in range(M)]

prev = 0
for i in statList:
    for _ in range(bisect_right(cha, statList[i])- prev):
        print(i)
    #print(bisect_right(cha, statList[i])- ans)
    prev = bisect_right(cha, statList[i])
'''
