import math


def main(a, b, m, z):
    temp = 0
    for j in range(1, m + 1):
        for k in range(1, b + 1):
            for c in range(1, a + 1):
                temp += j ** 2 / 4 - (k ** 2 + z) - 31 * (
                            73 * c ** 2 - 29) ** 5
    return temp


print(main(6, 6, 7, -0.6))
