N = int(input())
numList = list(map(int,input().split()))
numList.sort()

sum_val = 1
for elem in numList:
    if elem > sum_val:
        break
    sum_val += elem

print(sum_val)





'''
N = int(input())
numList = list(map(int,input().split()))
possible_sums = set()

def combination(idx, sum_val):
    if idx == N:
        possible_sums.add(sum_val)
        return
    
    combination(idx+1, sum_val)
    combination(idx+1, sum_val+numList[idx])

combination(0,0)

num = 1
while True:
    if num not in possible_sums:
        print(num)
        break
    num+=1
'''
