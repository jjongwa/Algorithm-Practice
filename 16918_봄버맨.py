# 봄버맨
R, C, N = map(int, input().split())
field = []
for _ in range(R):
    field.append(list(input()))
#print(field)
#print(field[1][3])
def find_bom(arr):
    bomList = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                bomList.append([i,j])
    return bomList

def afterbom(arr, location):
    global R, C
    for i in range(len(location)):
        x, y = location[i][0], location[i][1]
        if x-1 >= 0 and arr[x-1][y] == '.':
            arr[x-1][y] = 'O'
        if x+1 < R and arr[x+1][y] == '.':
            arr[x+1][y] = 'O'
        if y-1 >= 0 and arr[x][y-1] == '.':
            arr[x][y-1] = 'O'
        if y+1 < C and arr[x][y+1] == '.':
            arr[x][y+1] = 'O'


def reverse(arr):
    for i in range(R):
        for j in range(C):
            if field[i][j] == 'O':
                field[i][j] = '.'
            else:
                field[i][j] = 'O'
def printfield(arr):
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end='')
        print()
    



if N == 0:
    printfield(field)
elif N %2 == 0:
    for i in range(R):
        for j in range(C):
            print('O', end='')
        print()
else:
    loop = int(N/2)
    for _ in range(loop):
        li = find_bom(field)
        afterbom(field, li)
        reverse(field)

    printfield(field)