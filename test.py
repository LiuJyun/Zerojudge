# n = int(input())
#
# a = 0
# b = 1
# c = a + b
#
# for i in range(n):
#     if i == 0:
#         print(1)
#     else:
#         print(c)
#         a = b
#         b = c
#         c = a + b

n = int(input())
a = []
for i in range(n):
    a.append(input())
m = int(input())
for i in range(m):
    s = input()
    if s in a:
        print('yes')
    else:
        print('no')
        a.append(s)