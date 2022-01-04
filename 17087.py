# ¼û¹Ù²ÀÁú6
import sys

def gcd(arr):
    def g(x, y):
        while y: x, y = y, x % y
        return x
    a = arr[0]
    for b in arr[1:]:
        a = g(a, b)
    return a

N, S = map(int, input().split())
A = list(map(int,sys.stdin.readline().split()))
#print(A)
for i in range(len(A)):
    A[i] = abs(A[i]-S)
#print(A)
print(gcd(A))
