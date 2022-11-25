# python3
import numpy as np


def min_max(M, m, i, j, op):
    ops = {'-': lambda x, y: x - y,
           '+': lambda x, y: x + y,
           '*': lambda x, y: x * y}
    max_val = -np.inf
    min_val = +np.inf
    for k in range(i, j):
        a = ops[op[k]](M[i][k], M[k+1][j])
        b = ops[op[k]](M[i][k], m[k+1][j])
        c = ops[op[k]](m[i][k], M[k+1][j])
        d = ops[op[k]](m[i][k], m[k+1][j])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    digits = list(map(int, dataset[::2]))
    operations = list(dataset[1::2])
    n = len(digits)
    M = [[0] * n for _ in range(n)]
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = digits[i]
        m[i][i] = digits[i]
    for s in range(1, n):
        for i in range(n-s):
            j = i+s
            m[i][j], M[i][j] = min_max(M, m, i, j, operations)
    return M[0][n-1]




if __name__ == "__main__":
    print(find_maximum_value(input()))
