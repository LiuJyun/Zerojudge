from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_list(numbers):
    return reduce(gcd, numbers)

while True:
    try:
        n = int(input())
        numbers = []
        for i in range(n):
            numbers.append(int(input()))
        gcd_value = find_gcd_of_list(numbers)
        print(gcd_value)
    except:
        break