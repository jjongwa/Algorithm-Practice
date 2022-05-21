import sys
sys.stdin = open('input.txt', 'r')




N, X = map(int,input().split())
A = list(map(int,input().split()))

for i in A:
    if i < X:
        print(i,end=' ')        

