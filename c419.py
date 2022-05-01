n = int(input())

for i in range(n):
    print('_' * (n-1-i), '*' * (i+1), sep='')