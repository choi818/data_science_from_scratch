def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)