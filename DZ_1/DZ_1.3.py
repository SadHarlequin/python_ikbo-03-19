# <! 14 Вар K3>


def f(n, m):
    s = 0
    t = 0
    for i in range(1, n + 1):
        s += 72 * i ** 2 + abs(i)
    s *= 21
    for i in range(1, n + 1):
        t += i + 22 * i ** 2
    s -= t*m
    return s


print("{:.2e}".format(f(int(input()), int(input()))))
