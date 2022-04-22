import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse = 1)

check = [0 for _ in range(k+1)]

for i in coin:
    tmp = i
    while tmp <= k:
        check[tmp] += 1
        tmp += i
    print(check)
print(check)

