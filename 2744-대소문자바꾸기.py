import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
fi = [0  for _ in range(21)]
fi[1] = 1
for i in range(2,21):
    fi[i] = fi[i-1]+fi[i-2]
print(fi[n])