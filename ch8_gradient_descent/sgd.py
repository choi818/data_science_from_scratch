import random
import sys
sys.path.insert(0, 'G:/TEMP/data_science_from_scratch')
from ch4_linear_algebra.vector import scalar_multiply
from ch4_linear_algebra.vector import vector_subtract

# stochastic gradient descent
def in_random_order(data):
    """
        임의의 순서로 data의 index를 반환
    """
    indexes = [i for i, _ in enumerate(data)]   # 데이터 포인트의 인덱스를 list로 생성
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):

    data = zip(x, y)
    theta = theta_0                             # 첫 시작점
    alpha = alpha_0                             # 기본 이동 거리
    min_theta, min_value = None, float("inf")   # 시작할 때의 최솟값
    iterations_with_no_improvement = 0

    # 만약 100번 넘게 반복하는 동안 더 작아지지 않는다면 멈춤
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        if value < min_value:
            # 새로운 최솟값을 찾았다면 이 값을 저장하고
            # 기본 이동 거리로 다시 돌아감
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # 만약 최솟값이 줄어들지 않는다면 이동 거리를 축소
            iterations_with_no_improvement += 1
            alpha *= 0.9
        
        # 각 데이터 포인트에 대해 경사를 계산
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta
