a = 'Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday'.split(', ')
b = input()
print(a.index(b) if b in a else 'error')