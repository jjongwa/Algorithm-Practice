n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
ans = 0
now = numbers[0]
tmp  = 0
for num in numbers:
    if num == now:
        tmp += 1
    else:
        now = num
        tmp = 1
    now+=1
    ans = max(ans, tmp)
print(ans)