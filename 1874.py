import sys
n = int(sys.stdin.readline())
stack = []
ans = []
tri = 0
start = 1

for i in  range(n):
    num = int(sys.stdin.readline())
    while start <= num:
        stack.append(start)
        ans.append('+')
        start += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        tri = 1
        break

if tri == 0:
    for i in ans:
        print(i)   
