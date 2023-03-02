import math


def main(y):
    if y < 52:
        return y ** 3 + y ** 7 + y ** 2 / 74
    if 52 <= y < 120:
        return (y ** 3 / 27) ** 3 / 80 - 88 * math.atan(y) ** 2 - 14 * y ** 7
    if 120 <= y < 166:
        return 45 * y ** 10 - y ** 6
    if 166 <= y < 236:
        return 57 * (y ** 3 - 59 * y) ** 7 + 51 * math.tan(10 * y ** 2 -
                                                           y) ** 2 + 1
    if y >= 236:
        return 97 * math.cos(y / 84) ** 4 - math.log(y,
                                                     math.e) ** 3 - 23 * \
            math.log10(
                40 * y ** 2 - y) ** 2


print(main(163))
print(main(168))
print(main(69))
print(main(208))
print(main(179))
