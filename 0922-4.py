import sys
INT_MAX = sys.maxsize
n = int(input())
road = list(map(int, input().split()))

now = 0
for i in range(1,n):
    now += (i*road[i])

li = 0
ri = sum(road)

for i in range(n):
    li += road[i]
    ri -= road[i]
    print(li, ri)
    if li - ri > 0:
        limit = i
        break

ano = 0
for i in range(n):
    ano += (abs(i-limit)*road[i])

print(ano)    