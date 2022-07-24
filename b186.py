while True:
    try:
        a, b, c = map(int, input().split())
        if a // 10 > c // 2:
            print('{} 個餅乾，{} 盒巧克力，{} 個蛋糕。'.format(a, b + c // 2, c))
        else:
            print('{} 個餅乾，{} 盒巧克力，{} 個蛋糕。'.format(a, b + a // 10, c))
    except:
        break