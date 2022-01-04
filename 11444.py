n = int(input())

def mul_2by2(a,b):  # multiply 2*2 square
    ans = [[0,0] for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += (a[i][k] * b[k][j]) %1000000007    # 여기를 줄여야했다
    return ans


def mul_mul(mtx,n):
    if n == 1:
        return mtx
    if n%2 == 0:
        now = mul_mul(mtx,n//2)
        return mul_2by2(now,now)
    else:
        now = mul_mul(mtx,n-1)
        return mul_2by2(now,mtx)
    
base = [[1,1],[1,0]]
print((mul_mul(base,n)[0][1])%1000000007)
