#   수 이어쓰기
N = int(input())

len_N = len(str(N))
ans = 0

for i in range(len_N-1):
    ans += 9 * (10** i) * (i+1)

print(ans + (N - 10**(len_N-1) + 1) * len_N)
