import sys
sys.stdin = open('input.txt', 'r')

attend = [0 for _ in range(31)]
for i in range(28):
    attend[int(input())] += 1

for i in range(1,31):
    if attend[i] == 0:
        print(i)