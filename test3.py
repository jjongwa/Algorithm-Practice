import sys
sys.stdin = open('input.txt', 'r')
a, b = map(str, input().split())

na = int(a[2])*100 + int(a[1])*10 + int(a[0])
nb = int(b[2])*100 + int(b[1])*10 + int(b[0])
if int(na) < int(nb):
    for i in range(2,-1,-1):
        print(b[i],end='')
else:
    for i in range(2,-1,-1):
        print(a[i],end='')