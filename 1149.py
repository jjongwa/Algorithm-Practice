# RGB°Å¸®

N = int(input())
house = []
ansList = [[0,0,0] for _ in range(N)]
for i in range(N):
    house.append(list(map(int,input().split())))
ansList[0] = house[0]
for i in range(1,N):
    ansList[i][0] = min(ansList[i-1][1], ansList[i-1][2]) + house[i][0]
    ansList[i][1] = min(ansList[i-1][0], ansList[i-1][2]) + house[i][1]
    ansList[i][2] = min(ansList[i-1][0], ansList[i-1][1]) + house[i][2]


print(min(ansList[N-1][0], ansList[N-1][1], ansList[N-1][2]))