s = input().split(' ')

for i in range(len(s)):
    if s[i] != '':
        if i == len(s) - 1:
            print(s[i])
        else:
            print(s[i], end=' ')