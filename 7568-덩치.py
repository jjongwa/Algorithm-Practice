import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
mem = []
for _ in range(N):
    mem.append(list(map(int, input().split())))

ansList = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if mem[i][0] < mem[j][0] and mem[i][1] < mem[j][1]:
            cnt +=1
    ansList.append(cnt)

for ans in ansList:
    print(ans, end=' ')