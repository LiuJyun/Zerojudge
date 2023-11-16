na = 0
nb = 0
while True:
    a, b = input().split()
    #a:紫 b:靈夢
    if a == 'Game':
        if nb > na:
            print('悲慘的籌措起香油錢')
        else:
            print('螢火的蹤跡')
        break
    elif a == 'Scissors' and b == 'Paper' or a == 'Paper' and b == 'Stone' or a == 'Stone' and b == 'Scissors':
        print('紫獲勝')
    else:
        print('靈夢獲勝')

