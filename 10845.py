import sys
N = int(sys.stdin.readline())
queue = []
for i in range(N):
    commend = sys.stdin.readline().split()
    if commend[0] == 'push':
        queue.append(commend[1])
    elif commend[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif commend[0] == 'size':
        if not queue:
            print(0)
        else:
            print(len(queue))
    elif commend[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif commend[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])

