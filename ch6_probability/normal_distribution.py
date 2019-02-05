import math
from matplotlib import pyplot as plt

# probability density function of normal distribution
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

# cumulative distribution function of normal distribution
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# normal cdf의 역함수
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """
        이진 검색을 사용해서 역함수를 근사
    """

    # 표준정규분포가 아니라면 표준정규분포로 변환
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z, low_p = -10.0, 0         # normal_cdf(-10)는 0에 근접
    hi_z, hi_p = 10.0, 1            # nonmal_cdf(10)는 1에 근접
    
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # 중간 값
        mid_p = normal_cdf(mid_z)   # 중간 값의 누적분포 값을 계산
        if mid_p < p:
            # 중간 값이 너무 작다면 더 큰 값들을 검색
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # 중간 값이 너무 크다면 더 작은 값들을 검색
            hi_z, hi_p = mid_z, mid_p
        else:
            break
        
    return mid_z

# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
# plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
# plt.legend()
# plt.title("Various Normal pdfs")
# plt.show()

# plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
# plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
# plt.legend(loc=4)   # 우측 하단
# plt.title("Various Normal cdfs")
# plt.show()
