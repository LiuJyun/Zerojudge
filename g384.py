s = input()
total = 0
for i in s:
    total += ord(i) - 65 + 1
print(total)