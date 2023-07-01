a, b = map(int, input().split())
c = min(a, b)
d = max(a, b)
total = 0
for i in range(c, d + 1):
    if i % 2 == 0:
        total += i

print(total)
