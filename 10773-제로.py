import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
l = []
for _ in range(K):
    n = int(input())
    if n == 0:
        l.pop()
    else:
        l.append(n)

print(sum(l))