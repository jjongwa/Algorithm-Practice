N = int(input())
def minus(n, k):
    if n == 0:
        return '0'
    else:
        if n % 2 == 0:
            return minus(n//k, k) + '0'
        else:
            return minus(n//k+1, k) + '1'

ans = minus(N, -2)
print(ans == '0')
if ans == '0':
    print(ans)
else:
    print(ans[1:])