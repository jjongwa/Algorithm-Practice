import sys
N = int(sys.stdin.readline())

for i in range(N):
    sen = input()
    sen+=" "
    #print(sen)
    #print(len(sen))
    stack = []
    for j in sen:
        if j ==" ":
            while stack:
                print(stack.pop(),end="")
            print(" ",end="")
            #print(i)
        else:
            stack.append(j)
    print()
