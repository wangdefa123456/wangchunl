def test_returt():
    return 1,2


x,y = test_returt()
print(x)
print(y)

def func(*args):
    the_max = args[0]
    the_min = args[0]
    for i in args:
        if i > the_max:
            the_max = i
        elif i < the_min:
            the_min = i
    return {'max':the_max,'min':the_min}
res = func(7,-20,3,40,-5)
print(res)


def test_func(compute):
    result = compute(3,4)
    print(result)


def compute(x,y):
    return x + y


test_func(compute)


def test_func(compute):
    result = compute(3, 4)
    print(result)


def compute(x, y):
    return x * y


test_func(compute)


def test_func(compute):
    result = compute(3, 4)
    print(result)


def compute(x, y):
    return x - y


test_func(compute)