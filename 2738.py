n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b = list(map(int, input().split()))
    for j in range(m):
        a[i][j] += b[j]

for i in range(n):
    print(*a[i])