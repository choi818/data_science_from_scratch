import sys
sys.path.insert(0, 'G:/TEMP/data_science_from_scratch')
from ch4_linear_algebra.vector import dot
from ch5_statistics.dispersion import de_mean
from ch5_statistics.dispersion import standard_deviation

# covariance
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

# correlation
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0
