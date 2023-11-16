# movie = {'name':'Saving Private Ryan', #電影名稱
#          'year':1998, #電影上映年份
#          'director':'Steven Spielberg',#導演
#          'Writer': 'Robert Rodat', #編劇
#          'Stars':['Tom Hanks', 'Matt Damon', 'Tom Sizemore'],#明星
#          'Oscar ':['Best Director','Best Cinematography','Best Sound','Best Film Editing','Best Effects, Sound Effects Editing']
#          #獲得的奧斯卡獎項
#         }
#
# for i in movie['Stars']:
#     print(i)

# https://movies.yahoo.com.tw/movieinfo_main.html/id=13379

# import os
#
# file = 'test.txt'
# # f = open(file, 'w')
# # f.write('tessssst\n')
# # f.write('testttt')
# # f.close()
#
# if os.path.isfile(file):
#     f = open(file, 'r')
#     lines = f.readlines()
#     for l in lines:
#         print(l)
#     f.close()


c = -100567.123
if isinstance(c, float):
    print('{:.1f}'.format(c))
else:
    print(c)