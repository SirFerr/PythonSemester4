def main(x):
    if x < -33:
        return (x ** 2 / 41 + 6 * x ** 3 + 1) ** 4 - (
                33 * x ** 2 + x ** 3 / 61 + x) ** 2 - (
                87 + 44 * x ** 3) ** 7
    if -33 <= x < -11:
        return x ** 5
    if x >= -11:
        return (x ** 2 / 30) ** 4 / 97 + 45 * (x ** 2 / 45 - 1) ** 6


print(main(-85))
print(main(-48))
print(main(-83))
print(main(-70))
print(main(-18))
print(main(1))
