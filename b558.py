b = [1]
for i in range(500):
    b.append(b[i] + i + 1)

while True:
    try:
        n = int(input())
        print(b[n-1])

    except:
        break