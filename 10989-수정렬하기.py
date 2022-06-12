import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
l = []
for _ in range(N):
    n = int(input())   
    l.append(n)

l.sort()
for i in l:
    print(i)