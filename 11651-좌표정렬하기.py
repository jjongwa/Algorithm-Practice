import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append((x,y))

arr = sorted(arr, key=lambda x: (x[1], x[0]))
for a in arr:
    print(a[0], a[1])