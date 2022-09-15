k, n = map(int, input().split())
ans = []

# cnt 번째 자리 숫자 결정
def Choose(cnt):
    # 종료조건
    if cnt == n+1:
        print(*ans)
        return

    # 재귀호출 1~k
    for i in range(1, k+1):
        ans.append(i)
        Choose(cnt+1)
        ans.pop()

Choose(1)