
sentences = 'John ate an apple Oh John'
print(ord('A'), ord('Z'))

name = 0
blank = 0
n_s = ''

for s in sentences:
    if name == 0:
        if 65 <= ord(s) <= 90:
            name = 1
            n_s += 'X'
            blank = 0
        else:
            if blank == 1:
                n_s = n_s[:len(n_s)-1]
                n_s += ' '
                blank = 0
            n_s += s
    elif name == 1:
        if s == ' ':
            blank = 1
            name = 0
        n_s += 'X'

print(n_s)

