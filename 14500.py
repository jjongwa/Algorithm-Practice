#   테트로미노
N, M = map(int,input().split())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

#print(paper)

shape = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


def count(x,y):
    output = 0
    for i in range(19):
        tmp =  0
        for j in range(4):
            try:   
                next_x = x + shape[i][j][0]
                next_y = y + shape[i][j][1]
                tmp += paper[next_x][next_y]
            except IndexError:
                continue
        output = max(output, tmp)
    return output

ans =[]
for i in range(N):
    for j in range(M):
       ans.append(count(i,j))

print(max(ans)) 
        
          
