import math

def B(alpha, beta):
    """
        모든 확률 값의 합이 1이 되도록 해주는 정규화 값
    """
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:      # [0, 1] 구간 밖에서는 밀도가 없음
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)

