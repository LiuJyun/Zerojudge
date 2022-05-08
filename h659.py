k, w, s, e = map(int, input().split())

total = 0
if k <= 2:
    total = total + 20
else:
    total = total + 20 + (k - 2) * 5

total = total + (w // 2) * 5

if e >= 19 and s < 18:
    s = 18

if s == 18:
    total = total + 185
    if e > 19:
        s = 19
if s == 19:
    total = total + 195
    if e > 20:
        s = 20
if s == 20:
    total = total + 205
    if e > 21:
        s = 21
if s == 21:
    total = total + 215
    if e > 22:
        s = 22
if s == 22:
    total = total + 225
    if e > 23:
        s = 23

print(total)