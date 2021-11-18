from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    return fact(n)

    '''result = 1
    for i in range(1,n+1):
        result *= i
    return result'''

    '''if (n>1):
        return n*factorial(n-1)
    else:
        return 1'''



def decToBin(numStr):
    try:
        n=bin(int(numStr))
    except:
        return 'Error!'
    return n[2:]

def binToDec(numStr):
    try:
        n = int(numStr, 2)
    except:
        return 'Error!'
    return n

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result

def romanToDec(numStr):

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    str(numStr)
    i=0
    result = 0
    while i<len(numStr):
        temp=i
        for value, letters in romans:
            k = numStr[i:].find(letters)
            if k == 0:
                i+=len(letters)
                result+=value
                break
        if temp==i:
            return 'Error!'
    return result

