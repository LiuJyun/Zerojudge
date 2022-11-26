n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    x = (a + b) / 2
    y = (a - b) / 2
    if x < 0 or y < 0 or int(x) != x:
        print('impossible')
    else:
        print(int(x), int(y))