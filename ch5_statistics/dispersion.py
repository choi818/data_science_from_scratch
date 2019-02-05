import sys
sys.path.insert(0, 'G:/TEMP/data_science_from_scratch')
from ch5_statistics.central_tendency import mean
from ch5_statistics.central_tendency import quantile
from ch4_linear_algebra.vector import sum_of_squares
import math

# range
def data_range(x):
    return max(x) - min(x)

# variance
def de_mean(x):
    """
        x의 모든 데이터에서 평균을 뺌 (평균을 0으로 만들기 위해)
    """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """
        x에 두 개 이상의 데이터가 존재한다고 가정
    """
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

# standard deviation
def standard_deviation(x):
    return math.sqrt(variance(x))

# interquartile range
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


A = [1, 2, 3, 1, 2, 1, 4]
# print(standard_deviation(A))