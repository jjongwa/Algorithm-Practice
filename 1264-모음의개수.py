while True:
    word = input()
    if word == '#':
        break
    cnt = 0
    for w in word:
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
            cnt += 1
        if w == 'A' or w == 'E' or w == 'I' or w == 'O' or w == 'U':
            cnt += 1
    print(cnt)