A = [ 4, 5, 4, 6, 3, 3, 3, 1, 2, 7] 
cnt = [0 for _ in range(8)]	# A에서 나올 수 있는 원소의 최댓값 + 1 

for a in A:
	cnt[a] += 1
    
print(cnt)

for i in range(1, 8):
    for _ in range(int(cnt[i])):
        print(i, end= ' ')
