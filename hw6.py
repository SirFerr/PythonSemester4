def zero(x):
    if x[0] == 'R':
        return 0
    if x[0] == 'APL':
        return 1


def threeCSON(x):
    if x[3] == 'GO':
        return 3
    if x[3] == 'RDOC':
        return 4
    if x[3] == 'E':
        return 5


def secondCSON(x):
    if x[2] == 1957:
        return zero(x)
    if x[2] == 1990:
        return 2
    if x[2] == 1997:
        return threeCSON(x)


def threeTEX1957(x):
    if x[3] == 'GO':
        return 6
    if x[3] == 'RDOC':
        return 7
    if x[3] == 'E':
        return 8


def threeTEX1990(x):
    if x[3] == 'GO':
        return 9
    if x[3] == 'RDOC':
        return 10
    if x[3] == 'E':
        return 11


def secondTEX(x):
    if x[2] == 1957:
        return threeTEX1957(x)
    if x[2] == 1990:
        return threeTEX1990(x)
    if x[2] == 1997:
        return 12


def first(x):
    if x[1] == 'CSON':
        return secondCSON(x)
    if x[1] == 'TEX':
        return secondTEX(x)


def main(x):
    if x[4] == 'ROUGE':
        return first(x)

    if x[4] == 'OPA':
        return 13


print(main(['APL', 'TEX', 1997, 'E', 'ROUGE']))
print(main(['APL', 'TEX', 1997, 'RDOC', 'OPA']))
print(main(['APL', 'CSON', 1990, 'RDOC', 'ROUGE']))
print(main(['APL', 'TEX', 1957, 'E', 'ROUGE']))
print(main(['APL', 'TEX', 1990, 'RDOC', 'ROUGE']))

print(main(['APL', 'CSON', 1957, 'GO', 'ROUGE']))
