import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
print = sys.stdout.write
N = int(input())

count = [0 for _ in range(10001)]

for _ in range(N):
    n = int(input())
    count[n] += 1

for i in range(1, 10001):
    for j in range(count[i]):
        print(str(i))
        print("\n")