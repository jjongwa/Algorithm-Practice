grid = [[0 for _ in range(3)] for _ in range(4)]
cnt = 1
for x in range(4):
    for y in range(3):
        grid[x][y] += cnt
        cnt += 1


for i in range(4):
    print(*grid[i])
print()
n_grid = list(list(i) for i in zip(*grid[::-1]))

print(n_grid)
for i in range(3):
    print(*n_grid[i])
print()

n_grid2 = [[0 for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        n_grid2[i][j] = grid[j][3-1-i]


print(n_grid2)
for i in range(3):
    print(*n_grid2[i])
print()


n_grid3 = [[0 for _ in range(4)] for _ in range(3)]
for i in range(3):
    for j in range(4):
        n_grid3[i][j] = grid[3-1-j][i]


print(n_grid2)
for i in range(3):
    print(*n_grid3[i])
print()