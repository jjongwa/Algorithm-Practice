dic = {}
dic['a'] = 1, 3
dic['c'] = 2, 2
dic['b'] = 4, 1
dic['e'] = 3, 5

print(dic)
#{'a': 1, 'c': 2, 'b': 4, 'e': 3}

print(sorted(dic.items(), key = lambda x: x[1]))
#[('a', 1), ('c', 2), ('e', 3), ('b', 4)]

print(sorted(dic.items(), key = lambda x: x[1][1]))

print(sorted(dic.items(), reverse=True))
#[('e', 3), ('c', 2), ('b', 4), ('a', 1)]