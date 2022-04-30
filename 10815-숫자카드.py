## 이분 탐색 버전
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
N = int(input())
have = list(map(int,input().split()))
M = int(input())
find = list(map(int,input().split()))

have.sort()

def is_possible(mid):
    return mid <= max(have)

for i in find:
    lo = bisect_left(have, i)
    hi = bisect_right(have, i)
    if hi - lo == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')


    
'''
## dictionay 사용 버전
import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int,input().split()))
check = {}
for i in cards:
    check[i] = 1 

M = int(input())
numbers = list(map(int,input().split()))

for i in numbers:
    if i in check:
        print(1, end=' ')
    else:
        print(0, end=' ')
'''