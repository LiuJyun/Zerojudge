DP = [0]*101
n = int(input())
while True:
    if n == 0:
        break;

    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    for j in range(100, a-1, -1):
        if DP[j] < DP[j - a] + b:
            DP[j] = int(DP[j - a]) + b
            #print(DP[j])

    n -= 1

print(DP[100])