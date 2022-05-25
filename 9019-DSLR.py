import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def D(n):
    return (n*2) % 10000

def S(n):
    if n == 0:
        return 9999
    else:
        return n-1

def L(n):
    d1 = n // 1000
    return (n*10) % 10000 + d1

def R(n):
    d4 = n % 10
    return (n //10) + d4* 1000

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    dq = deque()
    dq. append((A,[]))
    visited = [0 for _ in range(10000)]
    while dq:
        num, stack = dq.popleft()
        if D(num) == B:
            for ans in stack:
                print(ans, end='')
            print("D")
            break
        else:
            if visited[D(num)] == 0:
                dq.append((D(num), stack+['D']))
                visited[D(num)] = 1
        if S(num) == B:
            for ans in stack:
                print(ans, end='')
            print("S")
            break
        else:
            if visited[S(num)] == 0:            
                dq.append((S(num), stack+['S']))
                visited[S(num)] = 1
        if L(num) == B:
            for ans in stack:
                print(ans, end='')
            print("L")
            break
        else:
            if visited[L(num)] == 0:
                dq.append((L(num), stack+['L']))
                visited[L(num)] = 1
        if R(num) == B:
            for ans in stack:
                print(ans, end='')
            print("R")
            break
        else:
            if visited[R(num)] == 0:
                dq.append((R(num), stack+['R']))
                visited[R(num)] = 1






