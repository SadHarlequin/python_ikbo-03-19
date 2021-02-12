# <! 14 Вар K3>
import math


def f(n):
    if n < 0:
        print("Input data cannot be less than zero")
        quit()
    elif n == 0:
        return 6
    elif n == 1:
        return 10
    else:
        return abs(f(n - 2)) - math.tan(f(n - 1))


print("{:.2e}".format(f(int(input()))))
