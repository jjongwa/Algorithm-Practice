import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    type = sys.stdin.readline().split()

    if type[0] == 'push':
        num = type[1]
        stack.append(num)
    elif type[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop() 
    elif type[0] == 'size':
        print(len(stack))
    elif type[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif type[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1]) 
