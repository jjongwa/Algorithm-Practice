s = input()
now = s[1]
change = s[4]
ans = []
for i in s:
    if i == now:
        ans.append(change)
    else:
        ans.append(i)
for i in ans:
    print(i, end='')

