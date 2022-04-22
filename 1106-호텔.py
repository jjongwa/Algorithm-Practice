import sys
input = sys.stdin.readline
C, N = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    city[i].append(city[i][1]/city[i][0])

city.sort(key=lambda x:x[2],reverse=True)
#print(city)

cus = 0
ans = 0
now = 0
while cus < C:
    if city[now][1]