import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
txt = {}
for _ in range(N):
    site, pw = map(str, input().strip().split())
    txt[site] = pw
for _ in range(M):
    st = input().strip()
    print(txt[st])