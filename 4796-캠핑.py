import sys
sys.stdin = open('input.txt', 'r')

i = 1
while True:
    L, P, V = map(int,input().split())
    if L == 0 and P == 0 and V == 0:
        break
    ans = V//P*L
    if V%P > L:
        ans += L
    else:
        ans += (V%P)
    print("Case", i,end=": ")
    print(ans)
    i += 1