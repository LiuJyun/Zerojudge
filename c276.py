s = input()
n = int(input())

for i in range(n):
    t = input()
    a = 0
    b = 0
    for j in range(len(s)):
        if s[j] == t[j]:
            a += 1
        elif s[j] in t and t.index(s[j]) != j:
            b += 1
    print('{}A{}B'.format(a, b))