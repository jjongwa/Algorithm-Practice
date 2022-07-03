n = 5
horizontal = 0

def check(arr, n):  # 설정한 범위 내에 체크된게 남아있으면 0을 리턴
    for x in range(n+1):
        for y in range(n+1):
            if arr[x][y] == 0:
                return 0
    return 1

def is_possible(x,y,n):
    return 0<= x <= n and  0<= y <= n

dx = (0,1,0,-1)
dy = (1,0,-1,0)

def solution(n, horizontal):
    chk = [[0 for _ in range(n+1)] for _ in range(n+1)]
    x, y = 0, 0
    cnt = 1
    chk[0][0] = cnt
    cnt += 1
    ho = horizontal
    while cnt <= n*n:
        print("cnt: ", cnt)
        if check(chk, n):
            break
        elif check(chk, max(x, y)):
            if ho == 1:
                y += 1
                chk[x][y] = cnt
                cnt += 1
                ho = 0
            elif ho == 0:
                x += 1
                chk[x][y] = cnt
                cnt += 1
                ho =  1
        else:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if is_possible(nx, ny, max(x,y)) and chk[nx][ny] == 0:
                    while is_possible(nx, ny, max(x,y)):
                        chk[nx][ny] = cnt
                        cnt += 1
                        nx, ny = nx+dx[i], ny+dy[i]
                        break
                    x, y = nx- dx[i], ny - dy[i]
                    print(x, y)
                    break
    answer = [[0 for _ in range(n)] for i in range(n)]
    for x in range(n):
        for y in range(n):
            answer[x][y] = chk[x][y]
    
    return answer

print(solution(n, horizontal))








-- 코드를 입력하세요
SELECT prr.created_at "MONTH", p.name "NAME", count(p.name) "COUNT"
from places p
join (select pr.id, pr.place_id, month(pr.created_at) created_at
      from place_reviews pr
)prr on prr.place_id = p.id
group by prr.created_at
order by prr.created_at, p.name


-- 코드를 입력하세요
select pr.id, pr.place_id, month(pr.created_at) created_at
from place_reviews pr
group by month(pr.created_at)
