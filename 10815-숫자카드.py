import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int,input().split()))
check = {}
for i in cards:
    check[i] = 1 

M = int(input())
numbers = list(map(int,input().split()))

for i in numbers:
    if i in check:
        print(1, end=' ')
    else:
        print(0, end=' ')