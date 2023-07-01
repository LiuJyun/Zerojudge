while True:
    n = int(input())

    if n == 0:
        break

    s = str(n)

    sum = 0
    for i in range(len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            sum -= int(s[i])

    if sum % 11 == 0:
        print('{} is a multiple of 11.'.format(n))
    else:
        print('{} is not a multiple of 11.'.format(n))