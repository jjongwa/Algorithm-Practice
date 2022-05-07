n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]      # 입구
summits = [5]    # 봉우리
answer = []


way = [[]for _ in range(n+1)]
for i in paths:
    way[i[0]].append([i[1], i[2]])
    way[i[1]].append([i[0], i[2]])
for i in way:
    i.sort(key=lambda x: (x[1], x[0]))
    print(i)


up, down =[], []

dp = [0 * (n+1)]
def dfs(start, now, end, inten, chk):
    chk[now] = 1
    for nxtPoint in way[now]:
        if chk[nxtPoint[0]] == 0 and nxtPoint[0] == end:
            tmp.append(max(inten, nxtPoint[1]))
        
        if chk[nxtPoint[0]] == 0 and nxtPoint[0] not in gates and nxtPoint[0] not in summits:
            dfs(start, nxtPoint[0], end, max(inten, nxtPoint[1]), chk)

        


ansList = []
for i in gates:
    for j in summits:
        print(i, j)
        chk = [0]*(n+1)
        tmp = []
        dfs(i, i, j, 0, chk)
        print(tmp)
        up = min(tmp)

        chk = [0]*(n+1)
        tmp = []
        dfs(j,j,i,0, chk)
        print(tmp)
        down = min(tmp)
        ansList.append([j, max(up, down)])
        print()

ansList.sort(key=lambda x: (x[1], x[0]))

print(ansList)

answer = ansList[0]

print(answer)




#ansList.sort(key=lambda x: (x[1], x[0]))


answer = ansList[0]

#print(answer)

'''
def dfs(start,now, cnt, summit):
    if summit == 0:
        chk[now] = 1
    else:
        chk[now] = 2

    if start == now and  summit != 0:
        print("등산 끝")
        ansList.append([cnt, summit])
        return    
    for nxtPoint in way[now]:
        if summit == 0 and chk[nxtPoint[0]] == 0:  # 아직 봉우리 못만남 -> 이전에 왔던 길은 제외 (chk가 1일 길)
            print(now, nxtPoint[0])
            if nxtPoint[0] in summits:
                print("봉우리")
                dfs(start, nxtPoint[0], cnt+nxtPoint[1], nxtPoint[0])
            else:    
                dfs(start, nxtPoint[0], cnt+nxtPoint[1], 0)
        # 봉우리 만나고 내려오는길
        elif summit != 0 and chk[nxtPoint[0]] != 2:
            if nxtPoint[0] not in summits:
                print(now, nxtPoint[0])
                print("하산")
                dfs(start, nxtPoint[0], cnt+nxtPoint[1], summit)

    #ansList.append([cnt, summit])
    print()

for i in gates:
    chk = [0]*(n+1)
    dfs(i, i, 0, 0)

print(ansList)















def dfs(start, now, summit, smtchk, cnt):
    if smtchk == 0:
        chk[now] = 1
    else:
        chk[now] = 2

    if start == now and  smtchk == 1:
        print("등산 끝")
        ansList.append([summit, cnt])
        return

    for nxtPoint in way[now]:
        if nxtPoint[0] != start and nxtPoint[0] in gates:
            continue
        if smtchk == 0 and chk[nxtPoint[0]] == 0:  # 아직 봉우리 못만남 -> 이전에 왔던 길은 제외 (chk가 1일 길)
            print(now, nxtPoint[0])
            if nxtPoint[0] == summit:
                print("봉우리")
                ansList.append()
                dfs(start, nxtPoint[0], summit, 1, max(cnt,nxtPoint[1]))
            elif nxtPoint[0] not in summits:    
                dfs(start, nxtPoint[0], summit, 0, max(cnt,nxtPoint[1]))
        # 봉우리 만나고 내려오는길
        elif smtchk == 1 and chk[nxtPoint[0]] != 2:
            if nxtPoint[0] not in summits:
                print(now, nxtPoint[0])
                print("하산")
                dfs(start, nxtPoint[0], summit, 1, max(cnt,nxtPoint[1]))


'''