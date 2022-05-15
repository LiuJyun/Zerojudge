a, b, c = map(int, input().split())
# n = abs((b - a) // c) + 1
# for i in range(n):
#     print(a, end=' ')
#     a = a + c
while True:
    print(a, end=' ')
    if a == b:
        break
    a = a + c