n = int(input())

for i in range(n):
    print('_' * (n-1-i), '*' * (2*(i+1)-1), '_' * (n-1-i), sep='')