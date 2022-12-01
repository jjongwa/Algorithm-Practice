k = 2
dic = ["slang", "badword"]
chat = "badword ab.cd bad.ord .word sl.. bad.word"
answer = ''

def check(k, bad, word):
    bad_len = len(bad)
    word_len = len(word)
    for w in range(word_len):
        if word[w] != '.' and word[w] not in bad:
            return 0
    if bad_len > word_len +k -1:
        return 0
    st = 0
    end = word_len -1
    bad_end = bad_len-1
    cnt = 0
    while word[st] != '.':        
        if word[st] != bad[st]:
            return 0
        st +=1
        cnt += 1
    while word[end] != '.':
        if word[end] != bad[bad_end]:
            return 0
        end -= 1
        bad_end -= 1
        cnt += 1

    if bad_len - cnt <= k:
        return 1
    else:
        return 0

chat_list = list(chat.split(' '))

for c in chat_list:
    tri = 0
    for d in dic:
        if len(c) > len(d):
            continue
        if c == d:
            tri = 1
        elif '.' in c and check(k*c.count('.'), d, c):
            tri = 1

        if tri == 1:
            for _ in range(len(c)):
                answer+= '#'
            break
    if tri == 0:
        answer+= c
    if c != chat_list[-1]:
        answer+= ' '
print(answer)