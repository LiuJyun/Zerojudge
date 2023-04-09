# while True:
#     try:
#         n = int(input())
#         for i in range(n):
#             print('=_=|||')
#     except:
#         break

while True:
    try:
        t = int(input())
        times = 0
        while True:
            print('=_=|||')
            times = times + 1
            if t == times:
                break
    except:
        break