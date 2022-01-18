from itertools import combinations
N, K = map(int,input().split())
words = []

ans = 0
if K < 5:
    print(0)
else:
    K -= 5
    must = {'a', 'n', 't', 'i', 'c'}
    input_al = []
    alpha = {ky: v for v, ky in enumerate(set(map(chr, range(ord('a'),  ord('z')+1)))- must)}
    for _ in range(N):
        tmp = 0
        for i in set(input())- must:
            tmp |=(1 << alpha[i])
        input_al.append(tmp)

    combi = (2**i for i in range(21))
    for i in combinations(combi, K):
        tmp2 = sum(i)
        count = 0
        for j in input_al:
            if tmp2 & j == j:
                count += 1
        ans = max(ans,count)

    print(ans)