# partial function application
from functools import partial
from functools import reduce

def exp(base, power):
    return base ** power

two_to_the = partial(exp, 2)
print(two_to_the(3))

square_of = partial(exp, power=2)
print(square_of(3))

# map
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
map_twice_xs = map(double, xs)
print(next(map_twice_xs))
list_doubler = partial(map, double)
partial_map_twice_xs = list_doubler(xs)
print(next(partial_map_twice_xs))

def multiply(x, y): return x * y
products = map(multiply, [1,2], [4,5])
print(next(products), next(products))

# filter
def is_even(x):
    """x가 짝수면 True, 홀수면, False"""
    return x %2 == 0

x_evens = [x for x in xs if is_even(x)]
filter_x_evens = filter(is_even, xs)
list_evener = partial(filter, is_even)
partial_filter_x_evens = list_evener(xs)

# reduce
x_product = reduce(multiply, xs)
print(x_product)
list_product = partial(reduce, multiply)
partial_reduce_x_product = list_product(xs)
