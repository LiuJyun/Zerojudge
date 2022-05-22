dic = []
n = int(input())
for i in range(n):
    dic.append(input())

m = int(input())
for j in range(m):
    s = input()
    if s in dic:
        print('yes')
    else:
        print('no')
        dic.append(s)