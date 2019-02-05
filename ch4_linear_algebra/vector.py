from functools import partial
from functools import reduce
import math

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

# vector의 각 성분별 합
vector_sum = partial(reduce, vector_add)

# vector의 각 성분별 합의 평균
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def scalar_multiply(c, vector):
    return [c * v_i for v_i in vector]

# 내적
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# 각 성분의 제곱의 합
def sum_of_squares(vector):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(vector, vector)

def magnitude(vector):
    return math.sqrt(sum_of_squares(vector))

# distance between two vectors
def squared_distnace(v, w):
    """(v_1 - w_1)^2 + ... + (v_2 - w_2)^2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

