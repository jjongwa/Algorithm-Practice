import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

ans = N // 5
N =  N % 5
if N == 0:
    print(ans)
else:
    while True:
        if N % 3 == 0:
            print(ans + N//3)
            break
        else:
            if ans > 0:
                N += 5
                ans -= 1
            else:
                print(-1)
                break
        
