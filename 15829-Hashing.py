import sys
sys.stdin = open('input.txt', 'r')

L = int(input())
word = input()

ans = 0
tmp = 1
for i in range(len(word)):
    ans = (ans + ((ord(word[i])-96) * tmp) % 1234567891) % 1234567891
    tmp = (tmp*31) % 1234567891
print(ans)