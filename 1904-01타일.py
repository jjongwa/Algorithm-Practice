import sys
input = sys.stdin.readline
N = int(input())

ans = [0 for _ in range(N+2)]
ans[1], ans[2] = 1, 2

for i in range(1, N-1):
    ans[i+2] = (ans[i] + ans[i+1])%15746

print(ans[N])

'''
one = N-2
zero = 1

fac = [1 for _ in range(N+1)]

for i in range(1,N+1):
    fac[i] = fac[i-1] *i

ans = 1
while one >= 0:
    #print((fac[zero+one] / fac[zero] / fac[one]))
    ans += (fac[zero+one] / fac[zero] / fac[one])
    zero += 1
    one -= 2

print(int(int(ans)%15746))
'''
