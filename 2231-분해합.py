import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for i in range(N):
    target = str(i)
    s = int(target)
    for j in range(len(target)):
        s += int(target[j])
    if s == N:
        print(i)
        break
    if i == N-1:
        print(0)

