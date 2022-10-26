n, m = map(int, input().split())
for _ in range(n):
    grid = input()
    for i in range(len(grid)-1, -1, -1):
        print(grid[i], end='')
    print()