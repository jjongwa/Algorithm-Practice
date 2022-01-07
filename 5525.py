N = int(input())
M = int(input())
S = input()

#print(N,M,S[0])
start1 = 0
nowN = 0
ans =0
for i in range(M):
    if start1 == 0:
        if S[i] == 'I':
            start1 = 1
    else:
        if S[i-1] == 'I' and S[i] == 'O':
            continue
        elif  S[i-1] == 'O' and S[i] == 'I':
            nowN += 1
            if nowN == N:
                ans += 1
                nowN -= 1
        else:
            start1= 0
            nowN = 0
            if S[i] == 'I':
                start1 = 1
    #print(S[i], start1, nowN, ans)

print(ans)