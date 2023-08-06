a = [int(x) for x in input().split()]
n = int(input())
s = 0
for i in a:
    if n + 30 >= i:
        s += 1
print(s)