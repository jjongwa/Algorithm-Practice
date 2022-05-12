import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
a, b, c = 0, 0, 0

a += T//300
T = T%300
b += T//60
T = T%60
c = T//10
T = T%10
if T == 0:
    print(a,b,c)
else:
    print(-1)
