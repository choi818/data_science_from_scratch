from collections import Counter

# mean
def mean(x):
    return sum(x) / len(x)

# median
def median(v):
    """v의 중앙값을 계산"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # 데이터의 개수가 홀수면 중앙값을 반환
        return sorted_v[midpoint]
    else:
        # 데이터의 개수가 짝수면 두 중앙값의 평균을 반환
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

# quantile
def quantile(x, p):
    """x의 p분위에 속하는 값을 반환"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

# mode
def mode(x):
    """최빈값이 하나보다 많으면 list를 반환"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

A = [1, 2, 3, 1, 2, 1, 4]


# print("mean:", mean(A))
# print("median:", median(A))
# print("0.5 quantile:", quantile(A, 0.5))
# print("mode:", mode(A))
