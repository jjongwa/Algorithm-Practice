dx = (0,1,0,-1)
dy = (1,0,-1,0)

now_direct = 0
now = [0,0]

cmd = input()
for i in cmd:
    if i == 'R':
        now_direct += 1
        if now_direct >3:
            now_direct -= 4
    elif i == 'L':
        now_direct -= 1
        if now_direct < 0:
            now_direct += 4
    elif i == 'F':
        now[0] += dx[now_direct]
        now[1] += dy[now_direct]
print(*now)