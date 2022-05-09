T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    #print(distance)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif distance > r1+r2:
        print(0)
    elif distance == r1+r2:
        print(1)
    else:
        if distance >= max(r1, r2):
            print(2)
        elif distance < max(r1, r2):
            if distance+ min(r1,r2) > max(r1,r2):
                print(2)
            elif distance+ min(r1,r2) == max(r1,r2):
                print(1)
            elif distance+ min(r1,r2) < max(r1,r2):
                print(0)