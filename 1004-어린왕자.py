T = int(input())
def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        Cx, Cy, r = map(int, input().split())
        if dist(x1,y1, Cx,Cy) < r and dist(x2,y2, Cx,Cy) > r:
            cnt += 1
        elif dist(x1,y1, Cx,Cy) > r and dist(x2,y2, Cx,Cy) < r:
            cnt += 1
    print(cnt)