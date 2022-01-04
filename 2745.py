#   진법 변환
dic ={'A': 10}
for i in range(0,11):
    dic[str(i)] = i
for i in range(11,36):
    dic[chr(ord('A')+i-10)] = i

#print(dic)
N, B = input().split()
B = int(B)
'''
print(len(N))
print(N, B)
print(type(N), type(B))
'''
ans = 0
e = 0
#print(type(N[len(N)-1]))
for i in range(len(N)-1,-1,-1):
   
    ans += B**e * dic[N[i]]
 
    e += 1

print(ans)

