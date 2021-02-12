# <! 14 Вар K3>
import math


def f(x, y, z):
    a = y ** 3 + y ** 2/7 - 26
    try:
        1/a
    except ZeroDivisionError:
        print("ZeroDivisionError founded")
        quit()
    else:
        return 72*z**2 + math.sin(z) - (y**8-y**6)/a - 35*x**5-23*y**4


print("{:.2e}".format(f(int(input()), int(input()), int(input()))))
