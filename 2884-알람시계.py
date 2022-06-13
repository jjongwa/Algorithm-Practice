import sys
sys.stdin = open('input.txt', 'r')

H, M = map(int,input().split())

if M >= 45:
    print(H, M-45)
elif M < 45:
    newM = 60 - (45-M)
    if H == 0:
        print(23, newM)
    else:
        print(H-1, newM)