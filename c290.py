N = input()
y = []
x = [int(a) for a in str(N)]
for i in range(len(x)):
  if i % 2 == 0:
    y.append(x[i])
    x[i] = 0
xs, ys = sum(x), sum(y)
print(abs(xs - ys))