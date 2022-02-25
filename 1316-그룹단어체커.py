N = int(input())
words = []
for _ in range(N):
    words.append(input())
ans = 0

for w in words:
    check = {}
    tri =0
    for c in w:
        if c not in check:
            check[c] = 1
            now = c
        else:
            if now != c:
                tri = 1
                break
            now = c
        
    if tri == 0:
        ans += 1


print(ans)