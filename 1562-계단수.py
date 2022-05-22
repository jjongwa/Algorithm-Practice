import sys
sys.stdin = open('input.txt', 'r')




N = int(input())
for _ in range(N):
    R, S = map(str,input().split())
    for i in range(len(S)):
        for j in range(int(R)):
            print(S[i],end='')
    print()