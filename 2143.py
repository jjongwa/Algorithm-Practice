from collections import defaultdict
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

#   for A
Asum = defaultdict(int)
for Astart in range(len(A)):
    Aend = Astart
    tmp = 0
    while Aend < len(A):
        tmp += A[Aend]
        #print(tmp)
        Asum[tmp] += 1
        Aend += 1

    tmp -= A[Astart]


Bsum = defaultdict(int)
for Bstart in range(len(B)):
    Bend = Bstart
    tmp = 0
    while Bend < len(B):
        tmp += B[Bend]
        #print(tmp)
        Bsum[tmp] += 1
        Bend += 1

    tmp -= B[Bstart]

Akey = sorted(Asum.keys())
Bkey = sorted(Bsum.keys())

left = 0
right = len(Bkey)-1
ans = 0
#print(Akey, Bkey)
while left < len(Akey) and right >= 0:
    if Akey[left] + Bkey[right] == T:
        ans += (Asum[Akey[left]] * Bsum[Bkey[right]])
        left += 1
        right -= 1
    elif Akey[left] + Bkey[right] > T:
        right -= 1
    else:
        left += 1

print(ans)