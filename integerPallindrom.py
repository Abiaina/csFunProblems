def integerPallindromCheck (num):
    numList = []
    digitCount = 0

    if num == None:
        return "false"
    elif num == 0:
        return "true"

    if num < 0:
        num *= -1

    while num > 0:
        numList.append(num%10)
        num //= 10
        digitCount += 1

    if numList[0:((digitCount//2) -1)] == numList[-1:-(digitCount//2)]:
        return "true"

    return "false"

print('test')

if integerPallindromCheck(None) == 'false':
    print("pass for nil values")
else:
    print("fails for nil values")

if integerPallindromCheck(1001) == 'true':
    print("pass for even digit length pallindrom number")
else:
    print("fails for even digit length pallindrom number")

if integerPallindromCheck(-1001) == 'true':
    print("pass for negative even digit length pallindrom number")
else:
    print("fails for even digit length pallindrom number")

if integerPallindromCheck(10101) == 'true':
    print("pass for odd digit length pallindrom number")
else:
    print("fails for odd digit length pallindrom number")

if integerPallindromCheck(-10101) == 'true':
    print("pass for odd digit length pallindrom number")
else:
    print("fails for odd digit length pallindrom number")

if integerPallindromCheck(2101) == 'false':
    print("pass for even digit length non-pallindrom number")
else:
    print("fails for odd digit length non-pallindrom number")

if integerPallindromCheck(0) == 'true':
    print("pass for 0")
else:
    print("fails for for 0")
