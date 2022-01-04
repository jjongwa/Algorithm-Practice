N, A, B, DA, DB = map(int, input().split())

courseA = abs(A-B)
courseB = N- courseA


def game(n, one, two):
    if n == 0 or n == -N or n == N:
        return 0
    if n+one > N:
        next_p = n+one - N
    else:
        next_p = n+one
    if n-one < -N:
        next_m = n-one + N
    else:
        next_m = n-one
    plus = 1 + game(next_p, two, one)
    minus = 1+ game(next_m, two, one)

    print(plus, minus)
    return min(plus,minus)

if DA % 2 == 0 and DB % 2 == 0 and courseA %2 ==1 and courseB %2 ==1:
    print('Evil Galazy')
else:
    print(min(game(courseA,DA,DB),game(courseB,DA,DB)))