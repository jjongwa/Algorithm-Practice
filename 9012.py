import sys
T = int(sys.stdin.readline())

for i in range(T):
    sen = input()
    stack=[]
    tr = 0
    for i in sen:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if not stack:
                print('NO')
                tr = 1
                break
            else:
                stack.pop()

    if not stack and tr == 0:
        print('YES')
    else:
        if tr == 0:
            print('NO')