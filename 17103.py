#   °ñµå¹ÙÈå ÆÄÆ¼¼Ç
t = int(input())

primeNum = [False, False] + [True] *999999
for i in range(2,1000001):
    if primeNum[i] == 1:
        for j in range(i*2,1000001,i): 
            primeNum[j] = 0

for i in range(t):
    N = int(input())
    ans = 0
    for j in range(N//2+1):
        if primeNum[j] and primeNum[N-j]:
            ans += 1

    print(ans)

