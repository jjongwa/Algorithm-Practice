n = int(input())
village = list(map(int, input().split()))
distance = village[len(village)-1] - village[0]
cnt = 0

for i in range(len(village)-1):
    now_distance = village[i+1] - village[i]
    if now_distance == distance:
        cnt += 1
    if now_distance < distance:
        distance = now_distance
        cnt = 1
print(cnt)
