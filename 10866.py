import sys
N = int(sys.stdin.readline())
deque = []
for i in range(N):
    commend = sys.stdin.readline().split()
    if commend[0] == 'push_front':
        deque.insert(0,commend[1])
    elif commend[0] == 'push_back':
        deque.append(commend[1])
    elif commend[0] == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    elif commend[0] == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif commend[0] == 'size':
        if not deque:
            print(0)
        else:
            print(len(deque))
    elif commend[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif commend[0] == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])