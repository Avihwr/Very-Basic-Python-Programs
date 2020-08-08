def add():
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    addi = num1 + num2
    print('ANSWER IS BELOW--->: ')
    return addi


def sub():
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    subt = num1 - num2
    print('ANSWER IS BELOW--->: ')
    return subt


def div():
    num1 = int(input('Enter NUMERATOR: '))
    num2 = int(input('Enter DENOMINATOR: '))
    if num2 == 0:
        print("Denominator cannot be 0")
    else:
        divi = num1 / num2
        print('ANSWER IS BELOW: ')
        return divi


def mul():
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    mult = num1 * num2
    print('ANSWER IS BELOW--->: ')
    return mult


def powr():
    num1 = int(input('Enter a base number: '))
    num2 = int(input('Enter its power: '))
    powe = num1 ** num2
    print('ANSWER IS BELOW--->: ')
    return powe


def fac():
    factorial = 1
    num = int(input('Enter a number: '))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        i = 1
        while i <= num:
            factorial = factorial * i
            i += 1
        print("The factorial of", num, "is", factorial)


n = 1
while n > 0:
    print(' ')
    print('SIMPLE CALCULATOR')
    print('***********************')
    print('1.ADDITION')
    print('2.SUBTRACTION')
    print('3.MULTIPLICATON')
    print('4.DIVISION')
    print('5.SOLVE POWERS')
    print('6.FACTORIAL')
    print(' ')
    x = int(input('Enter Your Choice: '))
    if x == 1:
        print(add())

    elif x == 2:
        print(sub())

    elif x == 3:
        print(mul())

    elif x == 4:
        print(div())

    elif x == 5:
        print(powr())

    elif x == 6:
        print(fac())

    else:
        print('INVALID CHOICE')

n += 1
