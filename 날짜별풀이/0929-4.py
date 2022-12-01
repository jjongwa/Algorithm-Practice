word = input()

def find(le, ri):
    length = ri - le + 1
    while True:
        if le-1 >=0 and ri+1 <len(word) and word[le-1] == word[ri+1]:
            length += 2
            le -=1
            ri += 1
        else:
            break
    return length

ans = 0
for i in range(len(word)):
    ans = max(ans,find(i, i))
    if i+1 <len(word) and word[i] == word[i+1]:
        ans = max(ans, find(i, i+1))

print(ans)