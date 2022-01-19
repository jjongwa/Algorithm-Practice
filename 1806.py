import sys
#input = sys.stdin.readline()
'''
N, S = map(int,input().split())
L = list(map(int,sys.stdin.readline().split()))

ansList = []

for i in range(1, N+1):
    p_left = 0 
    p_right = p_left + i  # pointer
    while p_right <= N:
        tmp = L[p_left:p_right]
        if sum(tmp) >= S:
            ansList.append(p_right - p_left)
        p_left += 1
        p_right += 1

if len(ansList) == 0:
    print(0)
else:
    print(min(ansList))    
'''
N, S = map(int, input().split())
nums = list(map(int, input().split()))

ansList = []
tmp = 0
end = 0

for start in range(N):
    while tmp < S and end < N:
        tmp += nums[end]
        end += 1
    if tmp >= S:
        ansList.append(end - start)
    tmp -= nums[start]


if len(ansList) == 0:
    print(0)
else:
    print(min(ansList))


