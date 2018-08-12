def getDigitMatchCount (num1, num2):
  digitMatchCount = 0
    # checks for nil and normalizes numbers
  if num1 == None or num2 == None:
      return digitMatchCount
  if num1 < 0:
       num1 *= -1
  if num2 < 0:
       num2 *= -1
  if num1 <= num2:
       min = num1
  else:
      min = num2

    # could check for same number here and use log10 to return number of digits that match

  while min > 0:
    if num1%10 == num2%10:
      digitMatchCount += 1
    num1 //= 10
    num2 //= 10
    min //= 10

  return digitMatchCount


# tests
print("tests")

if getDigitMatchCount(None, 101) == 0:
    print("pass for nil values")
else:
    print("fails for nil values")

if getDigitMatchCount(101, 101) == 3:
    print("pass for same number")
else:
    print("fails for same number")

if getDigitMatchCount(101, 222) == 0:
    print("pass for no similar digits number")
else:
    print("fails for no similar digits number")

if getDigitMatchCount(101, -101) == 3:
     print("pass for negative numbers with same digits")
else:
    print(getDigitMatchCount(101, -101))
    print("fails for negative numbers with same digits")
    print("---")

if getDigitMatchCount(101, -2101) == 3:
    print("pass for negative numbers with some similar digits")
else:
    print(getDigitMatchCount(101, -2101))
    print("fails for negative numbers with some similar digits")
    print("---")

if getDigitMatchCount(101, 2101) == 3:
    print("pass for numbers with some similar digits")
else:
    print(getDigitMatchCount(101, 2101))
    print("fails for numbers with some similar digits")
    print("---")

if getDigitMatchCount(101, 22222048562587234101) == 3:
    print("pass for large numbers with some similar digits")
else:
    print("fails for large numbers with some similar digits")
    print("---")

if getDigitMatchCount(0, 101) == 0:
    print("pass for 0")
else:
    print("fails for for 0")
