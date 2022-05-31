import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    n = int(input())
    cloths = {}
    for _ in range(n):
        a, b = map(str,input().split())
        if b not in cloths:
            cloths[b] = [a]            
        else:
            cloths[b].append(a)
    ans = 1
    for c in cloths:
        ans *= (len(cloths[c])+1)
    print(ans-1)