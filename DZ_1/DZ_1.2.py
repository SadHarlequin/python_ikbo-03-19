# <! 14 Вар K3>
import math


def f(x):
    if x < 71:
        return 72 * x ** 2 + math.sin(x)
    elif x < 151:
        return x ** 7 - x ** 3
    elif x < 163:
        return x**3+x**2/7-26
    elif x < 192:
        return x**5+abs(x)-82
    else:
        return 23*x+math.log(x)-97


print("{:.2e}".format(f(int(input()))))
