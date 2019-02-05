def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def partial_difference_quotient(f, v, i, h):
    """
        함수 f의 i번째 편도함수가 v에서 가지는 값
    """
    w = [v_j + (h if j == i else 0)     # h를 v의 i번째 변수에만 더한다
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]
