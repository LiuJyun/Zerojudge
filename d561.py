from decimal import Decimal
while True:
    try:
        s = '{:0.2f}'.format(Decimal(input()))
        if s == '-0.00':
            print('0.00')
        else:
            print(s)
    except:
        break