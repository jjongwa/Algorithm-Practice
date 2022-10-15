# ←, ↖, ↑, ↗, →, ↘, ↓, ↙ (45도 반시계 주의! - 물고기 이동)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
# 상어 (상좌하우) 연속해서 3칸 이동
shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

m, s = map(int, input().split()) # 물고기의 수, 연습 횟수
fish = [[[[], []] for _ in range(4)] for _ in range(4)]
fish_smell = [[0] * 4 for _ in range(4)]

x, y = map(int, input().split()) # 상어의 위치
x -= 1
y -= 1 # 인덱스로 인해 위치 재설정

for _ in range(m) :
    nnx, y, d = map(int, input().split()) # 물고기의 위치, 방향
    fish[nnx-1][y-1][0].append(d-1) # 해당 좌표에 방향 삽입


path = []
max_fish_count = -1

visited = [[False] * 4 for _ in range(4)]

# 1. 복제 마법 시전 (물고기 복제) 함수
def copy_start() :
    for i in range(4) :
        for j in range(4) :
            for dir in fish[i][j][0] :
                fish[i][j][1].append(dir)

# 2. 물고기 이동 함수
def move_fish() :
    position = []
    for i in range(4) :
        for j in range(4) :
            while fish[i][j][0] :
                nd = fish[i][j][0].pop()
                flag = False
                for _ in range(8) : # 8칸에 대하여 확인
                    nx = i + dx[nd]
                    ny = j + dy[nd]
                    # 이동할 수 있는 경우
                    if 0 <= nx < 4 and 0 <= ny < 4 and fish_smell[nx][ny] == 0 and not (nx == x and ny == y) :
                        position.append((nx, ny, nd))
                        flag = True
                        break
                    # 이동할 수 없는 경우
                    nd = (nd - 1) % 8
                if flag == False :
                    position.append((i, j, nd)) # 모두 이동할 수 없다면 이동 안함
    return position

def select_move_shark(r, c, fish_count, move_count, temp_path) :
    global x, y, visited, max_fish_count, path
    if move_count == 3 : # 3번 이동했다면
        if max_fish_count < fish_count :
            max_fish_count = fish_count
            path = [d for d in temp_path]
        return

    for d in range(4) : # 네 가지 방향에 대해서
        nx = r + shark_dx[d]
        ny = c + shark_dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 : # 범위를 벗어나지 않는다면
            if not visited[nx][ny] : # 방문한 적이 없다면
                visited[nx][ny] = True # 방문처리
                next_fish_count = fish_count + len(fish[nx][ny][0])
                select_move_shark(nx, ny, next_fish_count, move_count+1, temp_path+[d])
                visited[nx][ny] = False
            else :
                select_move_shark(nx, ny, fish_count, move_count+1, temp_path+[d])

def move_shark() :
    global x, y, fish, fish_smell
    for d in path :
        x = x + shark_dx[d]
        y = y + shark_dy[d]
        if fish[x][y][0] :
            fish[x][y][0] = []
            fish_smell[x][y] = 3 # 2가 아닌 3인 이유는 바로 다음 단계에서 1을 감소시키기 떄문

def reduce_smell() :
    global fish_smell
    for i in range(4) :
        for j in range(4) :
            if fish_smell[i][j] > 0 :
                fish_smell[i][j] -= 1

def copy_end() :
    global fish
    for i in range(4) :
        for j in range(4) :
            while fish[i][j][1] :
                fish[i][j][0].append(fish[i][j][1].pop())

for now in range(s) :
    # 1. 복제 마법 시전 (물고기 복제)
    copy_start()
    # 2. 물고기 이동
    position = move_fish()
    for r, c, dir in position :
        fish[r][c][0].append(dir)

    path = []
    max_fish_count = -1

    # 3. 상어 이동
    select_move_shark(x, y, 0, 0, [])
    move_shark()

    # 4. 냄새 감소
    reduce_smell()
    # 5. 복제 완료
    copy_end()

result = 0
for i in range(4) :
    for j in range(4) :
        result += len(fish[i][j][0])

print(result)