import sys
#input = sys.stdin.readline()
N, M = map(int,input().split())
A_list = list(map(int,sys.stdin.readline().split()))
#print(A_list)
ans = 0

for i in range(1,N+1):
    p_left = 0 
    p_right = p_left + i-1  # pointer
    tmp = 0
    for j in range(p_left,p_right+1):
        tmp += A_list[j]
    while p_right < len(A_list):
        if p_left != 0:
            tmp -= A_list[p_left-1]
            tmp += A_list[p_right]
        if tmp == M:
            ans += 1    
        p_left += 1
        p_right += 1

print(ans)    


'''
for i in range(1,N+1):
    win_size = i
    window = deque()
    for j in range(N):
        if len(window) < win_size:
            window.append(A_list[j])
        if len(window) == win_size:
            if sum(window) == M:
                ans +=1
            window.popleft()
'''


'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right<=N and left<=right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)

    if total == M:
        cnt += 1

        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)
'''