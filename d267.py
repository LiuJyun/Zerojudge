# 1
# Computers account for only 5% of the country's commercial electricity consumption.

n = int(input())
for i in range(n):
    s = input()

    dic = {}
    for j in s:
        if j.isalpha():
            if j.lower() in dic:
                dic[j.lower()] = dic[j.lower()] + j.lower()
            else:
                dic[j.lower()] = j.lower()
    d = sorted(dic, key=lambda x: (-len(dic[x]), x))
    for k in range(len(d)):
        if len(dic[d[k]]) == len(dic[d[0]]):
            print(d[k], end='')
        else:
            break
    print()