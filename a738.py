import math
while True:
  try:
    A,B=input().split()
    print(math.gcd(int(A),int(B)))
  except:
    break