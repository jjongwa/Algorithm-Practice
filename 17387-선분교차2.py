import sys
sys.stdin = open('input.txt', 'r')

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())



def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2-x1) * (y3- y1) - (y2-y1) * (x3-x1)
    if tmp >0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

if (ccw(x1, y1, x2, y2, x3, y3) == 0 or ccw(x1, y1, x2, y2, x4, y4) == 0) and (ccw(x3, y3, x4, y4, x1, y1) == 0 or ccw(x3, y3, x4, y4, x2, y2) == 0):
    if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <=max(y3,y4) and min(y3,y4) <= max(y1,y2):
        print(1)
    else:
        print(0)
elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
    print(1)
else:
    print(0)



if x1 < x2:
    a =  (y2-y1)/(x2-x1)
else:
    a =  (y1-y2)/(x1-x2)

if x4 < x4:
    b =  (y4-y3)/(x4-x3)
else:
    b =  (y3-y4)/(x3-x4)

if a == b:
    if min(x1,x2) < min(x3,x4):
        if max(x1,x2) < min(x3,x4):
            print(0)
        else:
            print(1)
    elif min(x1,x2) > min(x3,x4):
        if min(x1, x2) > max(x3,x4):
            print(0)
        else:
            print(1)
    else:
        print(0)
else:
    X = ( (y2-y1)/(x2-x1)*x1 - (y4-y3)/(x4-x3)*x3 + y3 - y1) / ( (y2-y1)/(x2-x1) - (y4-y3)/(x4-x3) )
    print(X)
    if x1<= X <= x2:
        print(1)
    else:
        print(0)
        