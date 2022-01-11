import copy
N, M = map(int, input().split())
stage = []
for _ in range(N):
    stage.append(list(input()))

#print(stage)
ans = 1e9

def move(count,nowstage):
    print('count',count)
    global ans
    o = []
    tmp = 0
    for i in range(N):
        for j in range(M):
            if nowstage[i][j] == 'o':
                o.append([i,j])
                tmp+=1
    print('tmp',tmp)
    if count >10:
        return
    elif tmp == 1:
        print('결론')
        ans = min(count, ans)
        return
    elif tmp == 0:
        return

    print(o[0][0],o[0][1],o[1][0],o[1][1])
    # left
    leftstage = copy.deepcopy(nowstage)

    print('원래꺼', leftstage)
    for i in range(len(o)):
        if o[i][1] == 0:
            print(o[i][0], o[i][1])
            leftstage[o[i][0]][o[i][1]] = '.'
        elif leftstage[o[i][0]][o[i][1]-1] == '#'or leftstage[o[i][0]][o[i][1]-1] == 'o':
            continue
        else:
            leftstage[o[i][0]][o[i][1]] = '.'
            leftstage[o[i][0]][o[i][1]-1] == 'o'
    if leftstage[o[0][0]][o[0][1]] != 'o' or leftstage[o[1][0]][o[1][1]] != 'o':
        print('left')
        print(leftstage)
        move(count+1, leftstage)

    #right
    rightstage = copy.deepcopy(nowstage)
    for i in range(len(o)):
        if o[i][1] == M-1:
            rightstage[o[i][0]][o[i][1]] = '.'
        elif rightstage[o[i][0]][o[i][1]+1] == '#' or rightstage[o[i][0]][o[i][1]+1] == 'o':
            continue
        else:
           
            rightstage[o[i][0]][o[i][1]] = '.'
            rightstage[o[i][0]][o[i][1]+1] == 'o'
    if rightstage[o[0][0]][o[0][1]] != 'o' or rightstage[o[1][0]][o[1][1]] != 'o':
        print('????')
        print('right')
        print(rightstage)
        move(count+1, rightstage)


    #up
    upstage = copy.deepcopy(nowstage)
    for i in range(len(o)):
        if o[i][0] == 0:
            upstage[o[i][0]][o[i][1]] = '.'
        elif upstage[o[i][0]-1][o[i][1]] == '#' or upstage[o[i][0]-1][o[i][1]] == 'o':
            continue
        else:
            upstage[o[i][0]][o[i][1]] = '.'
            upstage[o[i][0]-1][o[i][1]] ='o'
    if upstage[o[0][0]][o[0][1]] != 'o' or upstage[o[1][0]][o[1][1]] != 'o':
        print('up')
        print(upstage)
        move(count+1, upstage)


    #down
    downstage = copy.deepcopy(nowstage)
    for i in range(len(o)):
        if o[i][0] == N-1:
            downstage[o[i][0]][o[i][1]] = '.'
        elif downstage[o[i][0]+1][o[i][1]] == '#' or downstage[o[i][0]+1][o[i][1]] == 'o':
            continue
        else:
            downstage[o[i][0]][o[i][1]] = '.'
            downstage[o[i][0]+1][o[i][1]] == 'o'
    if downstage[o[0][0]][o[0][1]] != 'o' or downstage[o[1][0]][o[1][1]] != 'o':
        print('down')
        print(downstage)
        move(count+1, downstage)

move(0,stage)

if ans == 1e9:
    print(-1)
else:
    print(ans)