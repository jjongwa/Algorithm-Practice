from itertools import combinations
from collections import defaultdict

N, S = map(int, input().split())
nums = list(map(int,input().split()))

left = nums[:N//2]
right = nums[N//2:]

leftsum = defaultdict(int)              ####
rightsum = defaultdict(int)             ####
leftsum[0] = 1
rightsum[0] = 1

for i in range(1, len(left)+1):
    for j in combinations(left, i):
        leftsum[sum(j)] += 1

for i in range(1, len(right)+1):
    for j in combinations(right, i):
        rightsum[sum(j)] += 1

leftkey = sorted(leftsum.keys())
rightkey = sorted(rightsum.keys())
print(leftkey, rightkey)
ans = 0
l = 0 
r = len(rightkey)-1
#print(l, r)
while l < len(leftkey) and r >= 0:
    #print(l, r)
    #print(leftkey[l], rightkey[r])
    if leftkey[l] + rightkey[r] == S:
        #print(">>>>")
        ans += (leftsum[leftkey[l]] * rightsum[rightkey[r]])
        l += 1
        r -= 1
    elif leftkey[l] + rightkey[r] > S:
        r -= 1
    else:
        #print("???")
        l += 1


if S == 0:
    ans -= 1

print(ans)



'''
ans = 0
for i in range(1,N-1):
    numList = list(itertools.combinations(nums, i))
    for i in numList:
        if sum(i) == S:
            ans += 1

print(ans)
'''


