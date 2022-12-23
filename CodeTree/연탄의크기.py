def is_fit(radius, home):
    if home % radius:
        return 0
    else:
        return 1


n = int(input())
house = list(map(int, input().split()))
house.sort()
ans = 0
for radius in range(2, house[len(house) - 1] + 1):
    cnt = 0
    for h in house:
        cnt += is_fit(radius, h)
    ans = max(cnt, ans)

print(ans)
