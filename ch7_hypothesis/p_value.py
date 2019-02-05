from testing import normal_probability_above
from testing import normal_probability_below
from testing import mu_0, sigma_0
import random

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # 만약 x가 평균보다 크다면, x보다 큰 부분이 꼬리
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # 만약 x가 평균보다 작다면, x보다 작은 부분이 꼬리
        return 2 * normal_probability_below(x, mu, sigma)

# 동전의 앞면이 나온 경우가 530번 관측되었다면,
p_value = two_sided_p_value(531.5, mu_0, sigma_0)

# simulation
# extreme_value_count = 0
# for _ in range(100000):
#     num_heads = sum(1 if random.random() < 0.5 else 0   # 앞면이 나온 횟수
#                     for _ in range (1000))              # 동전을 1,000번 던져서
#     if num_heads >= 530 or num_heads <= 470:            # 극한 값이
#         extreme_value_count += 1                        # 몇 번 나오는지

# print('p_value:', p_value)
# print('simulation:', extreme_value_count / 100000)
