import sys
left =list(sys.stdin.readline())
left.pop()
right = []
M = int(sys.stdin.readline())

for i in range(M):
    n = sys.stdin.readline().split()
    if n[0] == 'L' and left:
        right.append(left.pop())
    elif n[0] == 'D' and right:
        left.append(right.pop())
    elif n[0] == 'B' and left:
        left.pop()
    elif n[0] == 'P':
        left.append(n[1])
        
print("".join(left)+ "".join(list(reversed(right))))



'''
stringlen = len(string)
cursor = stringlen

#print(string)

for i in range(M):
    n = sys.stdin.readline().split()
    if n[0] == 'L':
        if cursor != 0:
            cursor -=1
    elif n[0] == 'D':
        if cursor != stringlen:
            cursor +=1
    elif n[0] == 'B':
        if cursor != 0:
            del string[cursor-1]
            cursor -=1
            stringlen -=1
    elif n[0] == 'P':
        string.insert(cursor, n[1])
        cursor +=1
        stringlen+=1

    #print(n,string, cursor)
        
print("".join(string))
'''


