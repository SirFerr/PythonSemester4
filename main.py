a=1
a=a+a
a=a+a+a
a=a+a
print(a)

a=1
a=a+a
a=a+a
a=a+a
a=a+a
print(a)

a=1
b=a+a
b=b+b
b=b+b
a=b-(a-b)
print(a)

import random
def naive_mul(x, y):
    r = 0;
    for i in range(y):
        r +=x
    return r

random_inputs = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
for x, y in random_inputs:
    assert naive_mul(x, y) == x * y, f"{naive_mul(x, y)} != {x * y}"
print(x , y, naive_mul(x, y))

def fast_mul(x, y):
    result = 0
    while y > 0:
        if y % 2 == 1:
            result += x
        x = x << 1
        y = y >> 1
    return result

random_inputs = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
for x, y in random_inputs:
    assert fast_mul(x, y) == x * y, f"{fast_mul(x, y)} != {x * y}"
print(x , y, fast_mul(x, y))

def fast_pow(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        x = x * x
        y = y // 2
    return result

random_inputs = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(10)]
for x, y in random_inputs:
    assert fast_pow(x, y) == x ** y, f"{fast_pow(x, y)} != {x ** y}"
print(x , y, fast_pow(x, y))