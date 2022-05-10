N = int(input())
dots = []
for _ in range(N):
    dots.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    if i != N-1:
        ans += dots[i][0] * dots[i+1][1] - dots[i+1][0] * dots[i][1]
    elif i == N-1:
        ans += dots[i][0] * dots[0][1] - dots[0][0] * dots[i][1]
    
print(abs(ans/2))