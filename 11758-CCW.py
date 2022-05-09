x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = x1*y2+x2*y3+x3*y1 - y1*x2-y2*x3-y3*x1
    if tmp>0:
        print(1)
    elif tmp<0:
        print(-1)
    else:
        print(0)
ccw(x1, y1, x2, y2, x3, y3)


'''
def find_y(x1, y1, x2, y2, x3):
    return (y2-y1)/(x2-x1)*(x3-x1) + y1

if x2-x1 > 0 and y2-y1 > 0:
    vec = 1
    if find_y(x1, y1, x2, y2, x3) > y3:
        print(-1)
    elif find_y(x1, y1, x2, y2, x3) < y3:
        print(1)
    else:
        print(0)
elif x2-x1 > 0 and y2-y1 < 0:
    vec = 4
    if find_y(x1, y1, x2, y2, x3) > y3:
        print(-1)
    elif find_y(x1, y1, x2, y2, x3) < y3:
        print(1)
    else:
        print(0)
elif x2-x1 < 0 and y2-y1 > 0:
    vec = 2
    if find_y(x1, y1, x2, y2, x3) > y3:
        print(1)
    elif find_y(x1, y1, x2, y2, x3) < y3:
        print(-1)
    else:
        print(0)
elif x2-x1 < 0 and y2-y1 < 0:
    vec = 3
    
    if find_y(x1, y1, x2, y2, x3) > y3:
        print(1)
    elif find_y(x1, y1, x2, y2, x3) < y3:
        print(-1)
    else:
        print(0)
elif x1 == x2 and y1 != y2:
    if y2 > y1: # y축 정방향
        if x3 > x1:
            print(-1)
        elif x3 < x1:
            print(1)
        else:
            print(0)
    elif y2 < y1: # y축 역방향
        if x3 > x1:
            print(1)
        elif x3 < x1:
            print(-1)
        else:
            print(0)
              
elif y1 == y2 and x1 != x2:
    if x2 > x1: # x축 정방향
        if y3 > y1:
            print(1)
        elif y3 < y1:
            print(-1)
        else:
            print(0)
    elif x2 < x1:
        if y3 > y1:
            print(-1)
        elif y3 < y1:
            print(1)
        else:
            print(0)        
        
elif x1==x2 and y1==y2:
    print(0)

'''
