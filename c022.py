# n = int(input())
#
# for i in range(n):
#     a = int(input())
#     b = int(input())
#
#     sum = 0
#     for j in range(a, b + 1, 1):
#         if j % 2 == 1:
#             sum = sum + j
#     print('Case {}: {}'.format((i + 1), sum))

count = 0
t = int(input())
while True:
    total = 0
    n1 = int(input())
    n2 = int(input())
    for i in range(n1, n2 + 1, 2):
        total = total + i
    count = count + 1
    print('Case {}: {}'.format(count, total))
    if count == t:
        break