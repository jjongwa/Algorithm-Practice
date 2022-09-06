dx = (1,-1,0,0)
dy = (0,0,-1,1)

now = [0,0]

N = int(input())
for _ in range(N):
    d, l = map(str, input().split())
    l = int(l)
    if d == 'E':
        now[0] += (dx[0]*l)
        now[1] += (dy[0]*l)
    elif d == 'W':
        now[0] += (dx[1]*l)
        now[1] += (dy[1]*l)
    elif d == 'S':
        now[0] += (dx[2]*l)
        now[1] += (dy[2]*l)
    elif d == 'N':
        now[0] += (dx[3]*l)
        now[1] += (dy[3]*l)

print(*now)
