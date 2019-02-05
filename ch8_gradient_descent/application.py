import random
import sys
sys.path.insert(0, 'G:/TEMP/data_science_from_scratch')
from ch4_linear_algebra.vector import distance

def step(v, direction, step_size):
    """
        v에서 step_size만큼 이동하기
    """
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

# sum_of_squares의 미분값
def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

# 임의의 시작점 선택
v = [random.randint(-10, 10) for i in range(3)]
tolerance = 0.00001

def safe(f):
    """
        f와 똑같은 함수를 반환하지만
        f에 오류가 발생하면 무한대를 반환
    """
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.00001):
    """
        목적 함수를 최소화시키는 theta를
        경사 하강법을 사용해서 찾아준다
    """
    
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0             # theta를 시작점으로 설정
    target_fn = safe(target_fn) # 오류를 처리할 수 있는 target_fn으로 변환
    value = target_fn(theta)    # 최소화시키려는 값

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                        for step_size in step_sizes]
        
        # 함수를 최소화시키는 theta 선택
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # tolerance만큼 수렴하면 멈춤
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

# while True:
#     gradient = sum_of_squares_gradient(v)   # v의 경사도 계산
#     next_v = step(v, gradient, -0.01)       # 경사도의 음수만큼 이동
#     if distance(next_v, v) < tolerance:
#         break
#     v = next_v

# print(v)
