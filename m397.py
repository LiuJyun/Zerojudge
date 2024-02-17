pay, count, x_price, y_price = map(int, input().split())
y_count = (x_price * count - pay) / (x_price - y_price)
x_count = count - y_count
if y_count == int(y_count) and y_count >= 0 and x_count >= 0:
    print(int(x_count), int(y_count))
else:
    print(-1, -1)