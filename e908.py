w = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
a = input()
b = int(input())

print(w[(w.index(a) + b) % 7])