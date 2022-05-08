a, b = map(int, input().split())
if a * 60 + b >= 450 and a * 60 + b < 1020:
    print('At School')
else:
    print('Off School')