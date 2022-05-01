iFirstNumber, iSecondNumber = map(int, input().split())

if iFirstNumber == iSecondNumber:
    iGCD = iFirstNumber
    print(iGCD)

elif iFirstNumber > iSecondNumber:
    iDividend = iFirstNumber
    iDivisor = iSecondNumber

else:
    iDividend = iSecondNumber
    iDivisor = iFirstNumber

iRemainder=iDividend%iDivisor
while iRemainder != 0:
    iDividend = iDivisor
    iDivisor = iRemainder
    iRemainder=iDividend%iDivisor

iGCD = iDivisor
print(iGCD)