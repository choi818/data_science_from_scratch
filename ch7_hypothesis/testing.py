import math
import sys
sys.path.insert(0, 'G:/TEMP/data_science_from_scratch')
from ch6_probability.normal_distribution import normal_cdf
from ch6_probability.normal_distribution import inverse_normal_cdf

def normal_approximation_to_binomial(n, p):
    """
        Binomial(n, p)에 해당되는 mu(평균)와 sigma(표준편차) 계산
    """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# 누적분포함수는 확률변수가 특정 값보다 작을 확률을 나타낸다
normal_probability_below = normal_cdf

# 만약 확률변수가 특정 값보다 작지 않다면, 특정 값보다 크다는 것을 의미한다
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# 만약 확률변수가 hi보다 작고 lo보다 작지 않다면, 확률변수는 hi와 lo 사이에 존재한다
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# 만약 확률변수가 범위 밖에 존재한다면, 범위 안에 존재하지 않는다는 것을 의미한다
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    """
        P(Z <= z) = probability인 z값을 반환
    """
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """
        P(Z >= z) = probability인 z값을 반환
    """
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """
        입력한 probability 값을 포함하고
        평균을 중심으로 대칭적인 구간을 반환
    """
    tail_probability = (1 - probability) / 2

    # 구간의 상한은 tail_probability 값 이상의 확률 값을 갖고 있다
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # 구간의 하한은 tail_probability 값 이하의 확률 값을 갖고 있다
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    
    return lower_bound, upper_bound

# H0: p = 0.5, H1 = p != 0.5
# 동전을 1000번 던졌을 때, 앞면이 나올 평균과 표준편차
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
#print(mu_0, sigma_0)

# p가 0.5라고 가정할 때, 유의수준이 5%인 구간
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
# p = 0.55로 편할됐을 경우, 실제 평균과 표준편차
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# 제2종 오류란 귀무가설(H0)을 기각하지 못한다는 의미
# 즉, X가 주어진 구간 안에 존재할 경우를 의미
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
# print(power)

# H0: p <= 0.5, H1: p > 0.5
# 분포 상위 부분에 더 높은 확률을 주기 위해서
hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability
# print(power)
