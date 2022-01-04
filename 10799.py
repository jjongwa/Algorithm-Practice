S = list(input())
stack = []
stick = 0
ans = 0
tri = 0
for i in S:
    if i == '(':
        if tri == 1:
            stick += 1
            ans += 1
        stack.append(i)
        tri = 1
    elif i == ')':
        if tri == 1:
            stack.pop()
            ans += stick
            tri = 0
        elif tri == 0:
            stack.pop()
            stick -= 1
            tri = 0

print(ans)
