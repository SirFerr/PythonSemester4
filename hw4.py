def main(n):
    if n == 0:
        return -0.01
    if n == 1:
        return 0.09
    if n >= 2:
        return main(n - 1) ** 2 + 85 * main(n - 2) ** 3 - 24 * main(
            n - 1) ** 3


print(main(2))
