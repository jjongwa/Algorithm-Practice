import sys
sys.stdin = open('input.txt', 'r')

w =input()

for i in w:
    if i.isupper():
        print(i.lower(), end = "")
    else:
        print(i.upper(), end = "")
