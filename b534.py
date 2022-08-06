import math

def eratosthenes(n):
	isPrime = [True]*(n+1)
	isPrime[1] = False
	for i in range(2, int(n** 0.5) + 1):
		if  isPrime[i]:
			for j in range(i*i, n+1, i):
				isPrime[j] = False
	return [x for x in range(2,n+1) if isPrime[x]]

prime = eratosthenes(65536)

p = int(input())
for i in range(p):
    d = {}
    n, m = map(int, input().split())
    nn = n
    for i in range(2, n + 1):
        while n % i == 0:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

            n /= i
    s = ''
    for k, v in d.items():
        if v != 1:
            s += str(k) + '^' + str(v)
            # print(k, "^", v, sep="", end="")
        else:
            s += str(k)
            # print(k, sep="", end="")

        if k != list(d.keys())[-1]:
            s += '*'
            # print("*", end="")
    gcd = math.gcd(nn, m)
    # 2^2*3*5*547 , 20 , N
    if gcd in prime:
        print('{} , {} , Y'.format(s, gcd))
    else:
        print('{} , {} , N'.format(s, gcd))