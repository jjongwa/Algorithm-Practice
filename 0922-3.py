import sys
INT_MAX = sys.maxsize
N = int(input())
x, y = [], []
for _ in range(N):
    w, l = map(str, input().split())
    l = int(l)

    if w == 'E':
        x.append(l)
    elif w == 'W':
        x.append(-l)
    elif w == 'N':
        y.append(l)
    elif w == 'S':
        y.append(-l)
        
ans = INT_MAX
x_sum, y_sum = sum(x), sum(y)
for i in range(len(x)):
    ans = min(ans, abs(y_sum) + abs(x_sum - x[i]))

for i in range(len(y)):
    ans = min(ans, abs(x_sum) + abs(y_sum - y[i]))

print(ans)