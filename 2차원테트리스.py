from collections import deque
def pr(arr):
    for i in range(len(arr)):
        print(*arr[i])
    print()


k = int(input())
blue = deque([ deque([0]*4) for _ in range(4)] )
red = deque([ deque([0]*6) for _ in range(4)])
yellow = deque([ deque([0]*4) for _ in range(6)])
point = 0
def fill_red(x, t):
    if t == 0:
        y = 1
        while True:
            if y == 6 or red[x][y] == 1:
                break
            y += 1    
        red[x][y-1] = 1
                
    elif t == 1:
        y = 1
        while True:
            if y == 6 or red[x][y] == 1 or red[x+1][y] == 1:
                break
            y += 1    
        red[x][y-1] = 1
        red[x+1][y-1] = 1


def fill_yellow(y, t):
    if t == 0:
        x = 1
        while True:
            if x == 6 or yellow[x][y] == 1:
                break
            x += 1
        yellow[x-1][y] = 1
    elif t == 1:
        x = 1
        while True:
            if x == 6 or yellow[x][y] == 1 or yellow[x][y+1] == 1:
                break
            x += 1
        yellow[x-1][y] = 1
        yellow[x-1][y+1] = 1


def clear_red(y):
    for i in range(4):
        del(red[i][y])
        red[i].appendleft(0)

def clear_yellow(x):
    del(yellow[x])
    yellow.appendleft(deque([0,0,0,0]))

def chk_red():
    for x in range(4):
        for y in range(2):
            if red[x][y] == 1:
                return 1
    return 0

def chk_yellow():
    for x in range(2):
        for y in range(4):
            if yellow[x][y] == 1:
                return 1
    return 0


for _ in range(k):
    t, x, y = map(int, input().split())
    if t == 1:
        fill_red(x,0)
        fill_yellow(y,0)
    elif t == 2:
        fill_red(x,0)
        fill_red(x,0)
        fill_yellow(y,1)
    elif t == 3:
        fill_red(x,1)
        fill_yellow(y,0)
        fill_yellow(y,0)

    tmp = 0
    
    for jj in range(2,6):
        if red[0][jj] == 1 and red[1][jj] == 1 and red[2][jj] == 1 and red[3][jj] == 1:
            tmp += 1
            clear_red(jj)
            jj = 2        

    while chk_red():
        clear_red(5)

    for ii in range(2,6):
        if yellow[ii][0] == 1 and yellow[ii][1] == 1 and yellow[ii][2] == 1 and yellow[ii][3] == 1:
            tmp += 1
            clear_yellow(ii)
            ii = 2

    
    while chk_yellow():
        clear_yellow(5)

    
    point += tmp

    # pr(red)
    # pr(yellow)


print(point)

l = 0
for x in range(len(red)):
    l += sum(red[x])
for x in range(len(yellow)):
    l += sum(yellow[x])

print(l)
    