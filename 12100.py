N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

ansList = []
#print(max(map(max,board)))
def move(pan, cnt):
    if cnt == 5:
        ansList.append(max(map(max,pan)))
        return 
    
    left = [item[:] for item in pan]
    right = [item[:] for item in pan]
    up = [item[:] for item in pan]
    down = [item[:] for item in pan]

#left
    for i in range(N):
        j = 0
        while j < N-1:
            if left[i][j] == 0 and left[i][j+1] != 0:
                left[i][j] = left[i][j+1]
                left[i][j+1] = 0
                j =0            
            else:
                j +=1

    for i in range(N):
        j = 0
        while j < N-1:    
            if left[i][j] == left[i][j+1] and left[i][j] != 0:
                left[i][j] *=2
                left[i][j+1] = 0   
            else:
                j +=1

    for i in range(N):
        j = 0
        while j < N-1:
            if left[i][j] == 0 and left[i][j+1] != 0:
                left[i][j] = left[i][j+1]
                left[i][j+1] = 0
                j =0            
            else:
                j +=1
    '''
    for i in range(N):
        j = 0
        while j < N-1:
            if left[i][j] == 0 and left[i][j+1] != 0:
                left[i][j] = left[i][j+1]
                left[i][j+1] = 0
                j =0 
            elif left[i][j] == left[i][j+1] and left[i][j] != 0:
                left[i][j] *=2
                left[i][j+1] = 0
                 
            else:
                j +=1
    '''
    move(left,cnt+1)
    #print(left)

#right
    for i in range(N):
        j = N-1
        while j > 0:
            if right[i][j] == 0 and right[i][j-1] != 0:
                right[i][j] = right[i][j-1]
                right[i][j-1] = 0
                j =N-1                
            else:
                j -=1
    for i in range(N):
        j = N-1
        while j > 0:
            if right[i][j] == right[i][j-1] and right[i][j] != 0:
                right[i][j] *=2
                right[i][j-1] = 0 
            else:
                j -=1
    for i in range(N):
        j = N-1
        while j > 0:
            if right[i][j] == 0 and right[i][j-1] != 0:
                right[i][j] = right[i][j-1]
                right[i][j-1] = 0
                j =N-1                 
            else:
                j -=1

    '''
    for i in range(N):
        j = N-1
        while j > 0:
            if right[i][j] == 0 and right[i][j-1] != 0:
                right[i][j] = right[i][j-1]
                right[i][j-1] = 0
                j =N-1 
            elif right[i][j] == right[i][j-1] and right[i][j] != 0:
                right[i][j] *=2
                right[i][j-1] = 0
                
            else:
                j -=1
    '''
    move(right,cnt+1)



#up
    for j in range(N):
        i = 0
        while i < N-1:
            if up[i][j] == 0 and up[i+1][j] != 0:
                up[i][j] = up[i+1][j]
                up[i+1][j] = 0
                i =0 
            else:
                i +=1
    for j in range(N):
        i = 0
        while i < N-1:
            if up[i][j] == up[i+1][j] and up[i][j] != 0:
                up[i][j] *=2
                up[i+1][j] = 0              
            else:
                i +=1
    for j in range(N):
        i = 0
        while i < N-1:
            if up[i][j] == 0 and up[i+1][j] != 0:
                up[i][j] = up[i+1][j]
                up[i+1][j] = 0
                i =0               
            else:
                i +=1
    '''
    for j in range(N):
        i = 0
        while i < N-1:
            if up[i][j] == 0 and up[i+1][j] != 0:
                up[i][j] = up[i+1][j]
                up[i+1][j] = 0
                i =0 
            elif up[i][j] == up[i+1][j] and up[i][j] != 0:
                up[i][j] *=2
                up[i+1][j] = 0
                
            else:
                i +=1
    '''
    move(up,cnt+1)



#down
    for j in range(N):
        i = N-1
        while i > 0:
            if down[i][j] == 0 and down[i-1][j] != 0:
                down[i][j] = down[i-1][j]
                down[i-1][j] = 0
                i =N-1                
            else:
                i -=1
    for j in range(N):
        i = N-1
        while i > 0:
            if down[i][j] == down[i-1][j] and down[i][j] != 0:
                down[i][j] *=2
                down[i-1][j] = 0               
            else:
                i -=1
    for j in range(N):
        i = N-1
        while i > 0:
            if down[i][j] == 0 and down[i-1][j] != 0:
                down[i][j] = down[i-1][j]
                down[i-1][j] = 0
                i =N-1 
            else:
                i -=1
    '''
    for j in range(N):
        i = N-1
        while i > 0:
            if down[i][j] == 0 and down[i-1][j] != 0:
                down[i][j] = down[i-1][j]
                down[i-1][j] = 0
                i =N-1 
            elif down[i][j] == down[i-1][j] and down[i][j] != 0:
                down[i][j] *=2
                down[i-1][j] = 0
                
            else:
                i -=1
    '''
    move(down,cnt+1)


move(board, 0)
print(max(ansList))


# Aoh..