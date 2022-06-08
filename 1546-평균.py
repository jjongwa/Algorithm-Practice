import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
l = list(map(int, input().split()))

ans = 0
for i in l:
    ans += i/(max(l))*100
print(ans/N)
