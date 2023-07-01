n = int(input())
p = []
for i in range(n):
    p.append([int(x) for x in input().split()])

min_time = 999
max_time = -999

for i in range(1, len(p)):
    time = abs(p[i][0] - p[i-1][0]) + abs(p[i][1] - p[i-1][1])
    min_time = min(min_time, time)
    max_time = max(max_time, time)

print(max_time, min_time)
