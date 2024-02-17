f1 = {1: ['Medium Wac', 4], 2: ['WChicken Nugget', 8], 3: ['Geez Burger', 7], 4: ['ButtMilk Crispy Chicken', 6], 5: ['Plastic Toy', 3]}
f2 = {1: ['German Fries', 2], 2: ['Durian Slices', 3], 3: ['WcFurry', 5], 4: ['Chocolate Sunday', 7]}

total = 0
while True:
    c = int(input())
    if c == 0:
        print('Total: {}'.format(total))
        break

    n = int(input())
    if c == 1:
        total += f1[n][1]
        print(f1[n][0], f1[n][1])
    else:
        total += f2[n][1]
        print(f2[n][0], f2[n][1])
