n, t = map(int, input().split())
up = list(map(int, input().split()))
down = list(map(int, input().split()))

def mov():
    # up의 맨 오른쪽을 tmp1으로
    tmp1 = up[n-1]
    # up의 원소들을 각자 한칸씩 오른쪽으로
    for i in range(n-2,-1,-1):
        up[i+1] = up[i]
    
    tmp2 = down[n-1]
    for i in range(n-2,-1,-1):
        down[i+1] = down[i]

    up[0] = tmp2
    down[0] =tmp1

for i in range(t%(2*n)):
    mov()

for u in up:
    print(u, end=" ")
print()
for d in down:
    print(d, end=" ")
