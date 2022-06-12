import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

cnt = 1
now = 1
while now < N:
    now += cnt*6
    cnt += 1

print(cnt)