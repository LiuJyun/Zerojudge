a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

print('{}:{}'.format(sum(a), sum(b)))
print('{}:{}'.format(sum(c), sum(d)))

if sum(a) > sum(b) and sum(c) > sum(d):
    print('Win')
elif sum(a) < sum(b) and sum(c) < sum(d):
    print('Lose')
else:
    print('Tie')