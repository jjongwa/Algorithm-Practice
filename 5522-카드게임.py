import sys
sys.stdin = open('input.txt', 'r')
ans = 0
for _ in range(5):
    n = int(input())
    ans += n

print(ans)