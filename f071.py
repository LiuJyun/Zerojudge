a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

temp = False
sum = 0
for i in range(3):
    for j in range(5):
        if i == 2:
            if b[j] == a[2]:
                sum -= c[j]
                temp = True
        else:
            if a[i] == b[j]:
                sum += c[j]

if sum < 0:
    sum = 0
if not temp:
    sum *= 2
print(sum)