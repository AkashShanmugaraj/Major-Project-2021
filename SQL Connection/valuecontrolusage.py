from valuecontrol import integervaluecontrol, integernavigation
from math import factorial


def sqfun():
    val = integernavigation('Enter a number, i will square it!\n', homefunc=home)
    print(val**2)
def cufun():
    val = integernavigation('Enter a number, i will cube it!\n', homefunc=home)
    print(val**3)
def facfun():
    val = integernavigation('Enter a number, i will find the factorial!\n', homefunc=home)
    print(factorial(val))
def home():
    menu = '''Where do you what to go?
1. Square-er
2. Cuber-er
3. Factor-er
'''
    val = integervaluecontrol([1,2,3], menu, 'Only choose form Menu!')
    if val == 1:
        sqfun()
    elif val == 2:
        cufun()
    elif val == 3:
        facfun()

home()