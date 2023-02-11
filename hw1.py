import math


def main(x):
    return ((2 * (x ** 3) + ((x ** 3) / 6) ** 5) /
            (57 * (3 * x - (x ** 2) /
                   8 - (x ** 3) / 44) ** 6) -
            ((((math.log(x, 2)) ** 4) + 46) /
             (87 - 75 * (x ** 2)) ** 2))


print(main(0.29))
