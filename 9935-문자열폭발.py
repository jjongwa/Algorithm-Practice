initString = input()
bomb = input()


def checkIsBomb(stack, bomb):
    if len(stack) < len(bomb):
        return
    for i in range(len(bomb)):
        if stack[len(stack) - len(bomb) + i] != bomb[i]:
            return
    for _ in range(len(bomb)):
        stack.pop()


stack = []
for s in initString:
    stack.append(s)
    checkIsBomb(stack, bomb)

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))

# while True:
#     afterString = "".join(initString.split(bomb))
#     if initString == afterString:
#         break
#     initString = afterString
#
# if len(initString) == 0:
#     print("FRULA")
# else:
#     print(initString)
