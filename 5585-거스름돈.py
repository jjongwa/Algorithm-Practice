change = 1000 - int(input())

cnt = 0
while change > 0:
    if change >= 500:
        change -= 500
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    elif change >= 1:
        change -= 1
    cnt += 1
print(cnt)