import math

while True:
    try:
        n = int(input())
        for i in range(n):
            a = int(input())
            b = int(input())
            sum = 0
            for j in range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b)) + 1):
                sum += j**2
            print('Case {}: {}'.format(i+1, sum))
    except:
        break