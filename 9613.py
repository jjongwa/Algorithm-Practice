# GCDÇÕ
import sys
import math
t = int(input())

for i in range(t):
    arr = list(map(int,sys.stdin.readline().split()))
    k = arr.pop(0)
    sum = 0
    for l in range(k):
        for m in range(k):
            if l<m :
                sum += math.gcd(arr[l],arr[m])
    print(sum)
    #print(arr)
    #print(len(arr))




