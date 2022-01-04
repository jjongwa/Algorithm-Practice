#   날짜 계산
E, S, M = input().split()
#print(E, S, M)

clock = [1,1,1]
ans = 1

while True:
    if clock[0] == int(E) and clock[1] == int(S) and clock[2] == int(M):
        break
    clock[0] += 1
    clock[1] += 1
    clock[2] += 1
    ans += 1

    if clock[0] == 16:
        clock[0] = 1
    if clock[1] == 29:
        clock[1] = 1
    if clock[2] == 20:
        clock[2] = 1

    print(clock)

    

print(ans)



  
