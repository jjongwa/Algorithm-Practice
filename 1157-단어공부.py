import sys
sys.stdin = open('input.txt', 'r')

ansList = [0] * 26
hi = 0
word = input()
for w in word:
    if 65 <= ord(w) <= 90:
        ansList[ord(w)-65] += 1
    elif 97<= ord(w)<=122:
        ansList[ord(w)-97] += 1
tri = 0
for i in range(26):
    if hi < ansList[i]:
        hi = ansList[i]
        ans = i 
        tri = 0
    elif hi == ansList[i]:
        tri = 1
if tri:
    print('?')
else:
    print(chr(ans+65))
    