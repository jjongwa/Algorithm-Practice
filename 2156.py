#   포도주 시식

n = int(input())
wine = []
ansList = [[0,0,0] for _ in range(n+1)]
for k in range(n):
    wine.append(int(input()))
ansList[0][1] = wine[0]
#ansList[1][1] = wine[1]
#ansList[1][2] = ansList[0][1] + wine[1]
#print(wine)
#print(ansList)

for i in range(1,n):
    ansList[i][0] = max(ansList[i-1][0],ansList[i-1][1], ansList[i-1][2])
    ansList[i][1] = ansList[i-1][0] + wine[i]
    ansList[i][2] = ansList[i-1][1] + wine[i]
print(ansList)
print(max(ansList[n-1]))
