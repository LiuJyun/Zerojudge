n = int(input())
a = [int(x) for x in input().split()]

d = {}
for i in range(n):
    if a[i] in d:
        d[a[i]] += 1
    else:
        d[a[i]] = 1

max_count = 0
min_count = 999
for count in d.values():
    if count > max_count:
        max_count = count
    if count < min_count:
        min_count = count

print(max_count - min_count, max_count * 52 - n)

# 53
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 1
