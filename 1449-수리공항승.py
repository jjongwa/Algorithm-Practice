N, L = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

count = 0
cover = 0
for i in leak:
    if cover < i:
        count += 1
        cover = (i+L-1)
print(count)