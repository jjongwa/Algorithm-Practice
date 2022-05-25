import sys
sys.stdin = open('input.txt', 'r')

# top-down method
'''
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return f(n-1) + f(n-2)

print(f(int(input())))
'''

# top-down method - memoization
cache = [-1] * 91
cache[0], cache[1] = 0, 1

def f(n):
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]

print(f(int(input())))