import sys
INT_MAX = sys.maxsize
n = int(input())
road = list(map(int, input().split()))

le = 0
ri = sum(road)

for i in range(n):
    le += road[i]
    ri -= road[i]
    if le - ri > 0:
        limit = i
        break

ans = 0
for i in range(n):
    ans += (abs(i-limit)*road[i])

print(ans)