import math


def main(x):
    temp = 0
    for i in x:
        temp += 68 * math.cos(49 * i ** 3) ** 5
    return temp


print(main([0.52, -0.44, -0.59, 0.49, -0.36, -0.77]))
