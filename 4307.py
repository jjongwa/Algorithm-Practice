import sys
testCase = int(input())

for t in range(testCase):
    l, n = map(int,input().split())
    ansMin, ansMax = 0,0
    for i in range(n):
        ant = int(sys.stdin.readline().rstrip())
        ansMin = max(min(ant, l-ant), ansMin)
        ansMax = max(max(ant, l-ant), ansMax)
    
    print(ansMin, ansMax)