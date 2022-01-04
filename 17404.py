#   RGB거리 2

INf = float('inf')

N = int(input())
house = []
for i in range(N):
    house.append(list(map(int,input().split())))

ansList = []

for i in range(3):
    tmp = [[0,0,0] for _ in range(N)]
    for  j in range(3):
        if j == i:
            tmp[0][j] = house[0][j]
            continue
        tmp[0][j] = INf

    for j in range(1,N):
        tmp[j][0] = min(tmp[j-1][1], tmp[j-1][2]) + house[j][0]
        tmp[j][1] = min(tmp[j-1][0], tmp[j-1][2]) + house[j][1]
        tmp[j][2] = min(tmp[j-1][0], tmp[j-1][1]) + house[j][2]
        
    for j in range(3):
        if j == i:
            continue
        ansList.append(tmp[-1][j])

print(ansList)

























'''
# RGB거리

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
'''







































'''
N = int(input())
house = []
for i in range(N):
    house.append(list(map(int,input().split())))
ansList = [ [[0,0], [0,0], [0,0]] for _ in range(N) ]

ansList[0][0] = [house[0][0],0]
ansList[0][1] = [house[0][1],1]
ansList[0][2] = [house[0][2],2]
print(ansList)

for i in range(1,N):
    if ansList[i-1][1][0] < ansList[i-1][2][0]:
        ansList[i][0] = [ansList[i-1][1][0] + house[i][0], ansList[i-1][1][1]]
    else:
        ansList[i][0] = [ansList[i-1][2][0] + house[i][0], ansList[i-1][2][1]]

    if ansList[i-1][0][0] < ansList[i-1][2][0]:
        ansList[i][1] = [ansList[i-1][0][0] + house[i][1], ansList[i-1][0][1]]
    else:
        ansList[i][1] = [ansList[i-1][2][0] + house[i][1], ansList[i-1][2][1]]

    if ansList[i-1][0][0] < ansList[i-1][1][0]:
        ansList[i][2] = [ansList[i-1][0][0] + house[i][2], ansList[i-1][0][1]]
    else:
        ansList[i][2] = [ansList[i-1][1][0] + house[i][2], ansList[i-1][1][1]]    



#ansList[1][0] = [min(ansList[i-1][1][0], ansList[i-1][2][0]) + house[i][0], 0]

print(ansList)

'''


'''
for i in range(1,N):
    ansList[i][0] = min(ansList[i-1][1], ansList[i-1][2]) + house[i][0]
    ansList[i][1] = min(ansList[i-1][0], ansList[i-1][2]) + house[i][1]
    ansList[i][2] = min(ansList[i-1][0], ansList[i-1][1]) + house[i][2]


print(min(ansList[N-1][0], ansList[N-1][1], ansList[N-1][2]))

'''




'''
N = int(input())
color = []
for i in range(N):
    color.append(list(map(int,input().split())))

ansList =[[[0,0],[0,0],[0,0]]  for _ in range(N)]
ansList[0] = [[color[0][0],0],[color[0][1],1],[color[0][2],2]]

print(ansList)
if ansList[1][1][0] < ansList[1][2][0]:
    ansList[1][0] = ansList[0][1]
    ansList[1][0][0] = ansList[0][0][0] + color[1][1][0]
else:
    ansList[1][0] = ansList[0][2]
    ansList[1][0][0] = ansList[0][0][0] + color[1][2][0]

print(ansList[1])

for i in range(1,N-1):
    ansList[i][0] += min(ansList[i-1][1], ansList[i-1][2])
    ansList[i][1] += min(ansList[i-1][0], ansList[i-1][2])
    ansList[i][2] += min(ansList[i-1][0], ansList[i-1][1])



#print(ansList)
'''

