def doubler(f):
    def g(x):
        return 2 * f(x)

    return g

def f1(x): return x + 1
def f2(x, y): return x + y

g = doubler(f1)
print(g(3))

# random number of parameters
def magic(*args, **kwargs):
    print('unnamed args:', args)
    print('keyword args:', kwargs)

print(magic(1, 2, key="word", key2="word2"))

# fixed number of parameters
def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
print(other_way_magic(*x_y_list, **z_dict))

# correct doubler
def doubler_correct(f):
    """f의 인자에 상관없이 작동"""
    def g(*args, **kwargs):
        """g의 인자가 무엇이든 간에 f로 보내줌"""
        return 2 * f(*args, **kwargs)
    return g

g1 = doubler_correct(f1)
print(g1(4))
g2 = doubler_correct(f2)
print(g2(10, 20))
