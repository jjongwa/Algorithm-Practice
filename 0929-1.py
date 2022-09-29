n, x = map(int, input().split())

dp = [0] * ((n*(n+x))+1)
st = 1
while st <= n:
    for i in range(x+1):
        if dp[st*(st+i)] == 0:
            dp[st*(st+i)] =1
    st += 1

ans = n+1
while True:
    if dp[ans] == 1:
        print(ans)
        break
    ans +=1
