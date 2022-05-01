n = int(input())
score = [int(x) for x in input().split()]
score.sort()

worst = []
best = []
for i in range(len(score)):
    print(score[i], end=' ')
    if score[i] < 60:
        worst.append(score[i])
    else:
        best.append(score[i])
print()

worst.sort()
best.sort()

if len(worst) != 0:
    print(worst[-1])
else:
    print('best case')

if len(best) != 0:
    print(best[0])
else:
    print('worst case')