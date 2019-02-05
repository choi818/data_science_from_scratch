A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """(i, j)번째 원소가 entry_fn(i, j)인
    num_rows * num_cols list를 반환"""
    return [[entry_fn(i, j)             # i가 주어졌을 때, list를 생성
            for j in range(num_cols)]   # [entry_fn(i, 0), ...]
            for i in range(num_rows)]   # 각 i에 대해 하나의 list를 생성


def is_diagonal(i, j):
    """대각선의 원소는 1, 나머지 원소는 0"""
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)
# print(identity_matrix)
