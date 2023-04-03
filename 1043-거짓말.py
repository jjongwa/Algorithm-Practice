n, m = map(int, input().split())
truthList = set(input().split()[1:])

parties = []
for _ in range(m):
    parties.append(set(input().split()[1:]))

# print(parties)

for _ in range(m):
    for party in parties:
        if party & truthList:
            truthList = truthList.union(party)

ans = 0
for party in parties:
    if party & truthList:
        continue
    ans += 1

print(ans)

# for party in parties:
#     if party[0] != 1:
#         for i in range(1, len(party)):
#             if peoples[party[i]] == 1:
#                 chkParty(party)
#                 break
#
# # print(peoples)
#
# ans = 0
# for party in parties:
#     # print(party)
#     for i in range(1, len(party)):
#         if peoples[party[i]] == 1:
#             break
#         if i == len(party) - 1:
#             ans += 1
#             # print("ans+1")
#
# print(ans)
