import sys
sys.stdin = open('input.txt', 'r')

A, B, V = map(int, input().split())


day = (V-A) // (A-B)+1
hight = (day-1) * (A-B)
while True:
    hight += A
    if hight >= V:
        print(day)
        break
    hight -= B
    day += 1
