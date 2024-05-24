def test_func(compute):
    result = compute(4, 5)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)


def test_func(compute):
    result = compute(5, 6)
    print(result)


test_func(lambda x, y: x + y)


def test_func(compute):
    result = compute(5, 6)
    print(result)


test_func(lambda x, y: x * y)


def test_func(compute):
    result = compute(5, 6)
    print(result)


test_func(lambda x, y: x - y)