import math
import random
import sys
from collections import Counter
from matplotlib import pyplot as plt
sys.path.insert(0, 'G:/TEMP/data_science_from_scratch')
from ch6_probability.normal_distribution import inverse_normal_cdf
from ch5_statistics.correlation import correlation
from ch4_linear_algebra.matrix import shape
from ch4_linear_algebra.matrix import get_column
from ch4_linear_algebra.matrix import make_matrix

### one-dimensional
def bucketize(point, bucket_size):
    """
        각 데이터를 bucket_size의 배수에 해당하는 구간에 위치시킨다
    """
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """
        구간을 생성하고 각 구간 내 데이터 개수를 계산
    """
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

random.seed(0)

# -100과 100 사이의 균등분포
uniform = [200 * random.random() - 100 for _ in range(10000)]

# 평균이 0이고 표준편차가 57인 정규분포
normal = [57 * inverse_normal_cdf(random.random())
          for _ in range(10000)]

# plot_histogram(uniform, 10, "Uniform Histogram")
# plot_histogram(normal, 10, "Normal Histogram")


### two-dimensional
def random_normal():
    """
        표준정규분포를 따르는 임의의 데이터를 반환
    """
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

# joint distribution
plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Very Different Joint Distributions")
plt.show()

print(correlation(xs, ys1))
print(correlation(xs, ys2))

### high-dimensional
def correlation_matrix(data):
    """
        (i, j)번째 항목이 i번째 차원과 j번째 차원의 상관관계를 나타내는
        num_columns x num_columns 행렬 반환
    """
    _, num_columns = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)

_, num_columns = shape(data)
fig, ax = plt.subplots(num_columns, num_columns)

for i in range(num_columns):
    for j in range(num_columns):

        # x축은 j번째 열을, y축은 i번째 행을 나타내는 산포도
        if i != j:
            ax[i][j].scatter(get_column(data, j), get_column(data, i))

        # 만약 i == j, series라는 제목 출력
        else:
            ax[i][j].annotate("series" + str(i), (0.5, 0.5),
                              xycoords='axes fraction',
                              ha="center", va="center")
        
        # 왼쪽과 밑에 위치한 차트에만 축 레이블 명시
        if i < num_columns - 1: ax[i][j].xaxis.set_visible(False)
        if j > 0: ax[i][j].yaxis.set_visible(False)

# 밑에서 가장 오른쪽, 그리고 왼쪽에서 가장 위에 위치한 차트 안에는
# 문자열만 있기 때문에 축 레이블을 고정
ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_ylim(ax[0][1].get_ylim())

plt.show()
