dic = {'A': 10, 'J': 18, 'S': 26, 'B': 11, 'K': 19, 'T': 27, 'C': 12, 'L': 20, 'U': 28, 'D': 13, 'M': 21, 'V': 29,
     'E': 14, 'N': 22, 'W': 32, 'F': 15, 'O': 35, 'X': 30, 'G': 16, 'P': 23, 'Y': 31, 'H': 17, 'Q': 24, 'Z': 33,
     'I': 34, 'R': 25}

d = sorted(dic.items(), key=lambda x: x[0])

while True:
    try:
        for i in range(len(d)):
            d[i] = list(d[i])
            d[i][1] = d[i][1] // 10 + d[i][1] % 10 * 9

        a = input()
        s = 0
        for i in range(8):
            s += int(a[i]) * (8 - i)

        for i in range(len(d)):
            s += d[i][1]
            m = s % 10
            c = 10 - m
            s -= d[i][1]
            if c == 10:
                c = 0
            if c == int(a[8]):
                print(d[i][0], end='')
    except:
        break