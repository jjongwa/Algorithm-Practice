#   µ¿¹°¿ø
'''
N =  int(input())
ansList = [[1,1,1]] + [[0,0,0]] * (N-1)
print(ansList)
for i in range(1,N):
    print(ansList[i])
    ansList[i][0] = ansList[i-1][0] + ansList[i-1][1] + ansList[i-1][2]
    print(ansList[i])
    ansList[i][1] = ansList[i-1][0] + ansList[i-1][2]
    print(ansList[i])
    ansList[i][2] = ansList[i-1][0] + ansList[i-1][1]
    print(ansList[i])
    
    print()
    print(ansList)
    print()
    #print(ansList[i])
#print(ansList[0])
#print(ansList[1])

print((ansList[N-1][0]+ansList[N-1][1]+ansList[N-1][2]) % 9901)

'''

'''
N =  int(input())
ansList = [[1,1,1]] + [[0,0,0] for _ in range(N-1)]
#print(ansList)
for i in range(1,N):
    #print(ansList[i])
    ansList[i][0] = (ansList[i-1][0] + ansList[i-1][1] + ansList[i-1][2]) % 9901
    #print(ansList[i])
    ansList[i][1] = (ansList[i-1][0] + ansList[i-1][2]) % 9901
    #print(ansList[i])
    ansList[i][2] = (ansList[i-1][0] + ansList[i-1][1]) % 9901
    #print(ansList[i])
    
    #print()
    #print(ansList[i][0])
    #print()
    #print(ansList[i])
#print(ansList[0])
#print(ansList[1])

print((ansList[N-1][0]+ansList[N-1][1]+ansList[N-1][2]) % 9901)
'''


N =  int(input())
ansList = [[1,1,1]] + [[0,0,0]] * (N-1)
print(ansList)


ansList = [[1,1,1]] + [[0,0,0] for _ in range(N-1)]
print(ansList)









'''
n = int(input())
dp = [[0, 0, 0] for _ in range(n + 1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901
    print(dp[i])
print(sum(dp[n]) % 9901)
'''