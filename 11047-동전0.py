import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
count = 0
for i in range(N-1, -1, -1):
    count += (int(K/A[i]))
    K %= A[i]
    #print(f'coin:{A[i]}, K:{K}, ans:{count}')
    if K == 0:
        print(count)
        break
    
