#   ½ºÆ¼Ä¿
T = int(input())
for k in range(T):
    n = int(input())
    sticker = []
    ansList = [[0,0,0] for _ in range(n+1)]
    sticker.append(list(map(int,input().split())))
    sticker.append(list(map(int,input().split())))
    ansList[1] = [sticker[0][0], sticker[1][0], 0]
    #print(ansList)
    #print(sticker)
    for i in range(2,n+1):
        #print(ansList[i])
        ansList[i][0] = max(ansList[i-1][1],ansList[i-1][2]) + sticker[0][i-1]
        ansList[i][1] = max(ansList[i-1][0],ansList[i-1][2]) + sticker[1][i-1]
        ansList[i][2] = max(ansList[i-1][0],ansList[i-1][1]) 

    print(max(ansList[n]))


