import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
building = [[0 for _ in range(15)] for _  in range(15)]
for i in range(1,15):
    building[0][i] = i

for i in range(1,15):
    for j in range(1, 15):
        building[i][j] = building[i][j-1] + building[i-1][j]

print(building)
for _ in range(T):
    k = int(input())
    n = int(input())
    print(building[k][n])
