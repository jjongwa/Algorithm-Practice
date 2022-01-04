#   1, 2, 3 ´õÇÏ±â 5
ansList = [[0,0,0] for _ in range(100001)]
ansList[1] = [1,0,0]
ansList[2] = [0,1,0]
ansList[3] = [1,1,1]
for i in range(4,100001):
    ansList[i][0] = ansList[i-1][1] % 1000000009 + ansList[i-1][2] % 1000000009
    ansList[i][1] = ansList[i-2][0] % 1000000009 + ansList[i-2][2] % 1000000009
    ansList[i][2] = ansList[i-3][0] % 1000000009 + ansList[i-3][1] % 1000000009


    
T  = int(input())
for i in range(T):
    n = int(input())
    print(sum(ansList[n])%1000000009)