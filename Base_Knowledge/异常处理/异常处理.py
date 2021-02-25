try:
    num1 = int(input('n1>>'))
    num2 = int(input('n2>>'))
    print(num1 + num2)
except ValueError as e:
    print(e)


try:
    a = 0
    a.abc
except AttributeError as e:
    print(e)


try:
    print(ooo)
except NameError as e:
    print(e)


