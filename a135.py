# i = 1
# while True:
#     try:
#         s = input()
#         if s == 'HELLO':
#             print('Case {}: ENGLISH'.format(i))
#         elif s == 'HOLA':
#             print('Case {}: SPANISH'.format(i))
#         elif s == 'HALLO':
#             print('Case {}: GERMAN'.format(i))
#         elif s == 'BONJOUR':
#             print('Case {}: FRENCH'.format(i))
#         elif s == 'CIAO':
#             print('Case {}: ITALIAN'.format(i))
#         elif s == 'ZDRAVSTVUJTE':
#             print('Case {}: RUSSIAN'.format(i))
#         elif s == '#':
#             break
#         else:
#             print('Case {}: UNKNOWN'.format(i))
#
#         i = i + 1
#     except:
#         break

dic = {'HELLO': 'ENGLISH',
       'HOLA': 'SPANISH',
       'HALLO': 'GERMAN',
       'BONJOUR': 'FRENCH',
       'CIAO': 'ITALIAN',
       'ZDRAVSTVUJTE': 'RUSSIAN'}

i = 1
while True:
    try:
        s = input()
        if s in dic:
            print('Case {}: {}'.format(i, dic[s]))
        elif s == '#':
            break
        else:
            print('Case {}: UNKNOWN'.format(i))
        i = i + 1
    except:
        break