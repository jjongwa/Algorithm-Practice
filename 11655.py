# ROT13

S = list(input())
ans = []

for i in S:
    if i.isalpha():
        ROT13 = ord(i)+13
        if i.isupper():
            if ROT13 > 90:
                ROT13 -= 26
        elif i.islower():
            if ROT13 > 122:
                ROT13 -= 26
        ans.append(chr(ROT13))
    else:
        ans.append(i)
        
print(''.join(ans))
        