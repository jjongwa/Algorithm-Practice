n, m = map(int, input().split())
ans = []

# curr_num 번째 아이템을 포함할지 말지 (0/1)
# cnt: 몇개의 아이템(1)이 포함되었는지
def Combination(curr_num, cnt):
    # 종료조건
    if curr_num == n+1:
        if cnt == m:
            print(*ans)
        return

    # curr_num 이 포함 되는경우
    ans.append(curr_num)
    Combination(curr_num+1, cnt+1)
    ans.pop()

    # curr_num 이 포함되지 않는 되는경우
    Combination(curr_num+1, cnt)

    # 순서 바꾸면 내림차순 된다.

Combination(1,0)