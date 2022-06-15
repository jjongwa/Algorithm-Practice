import sys
sys.stdin = open('input.txt', 'r')

while True:
    word = input()
    if len(word) == 1 and word[0] == '.':
        break 
    stack = []
    tri = 0
    for w in word:
        if w == "(":
            stack.append(1)
        elif w == "[":
            stack.append(2)
        elif w == ")":
            if len(stack) > 0 and stack[len(stack)-1] == 1:
                stack.pop()
            else:
                tri = 1
                break
        elif w == "]":
            if len(stack) > 0  and stack[len(stack)-1] == 2:
                stack.pop()
            else:      
                tri = 1
                break
    if tri == 1 or len(stack) >0:
        print("no")
    elif tri == 0:
        print("yes")

        