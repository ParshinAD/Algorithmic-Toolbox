# python3
import numpy as np


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    add = (lambda x: 0, lambda x: x-1)
    double_value = (lambda x: x % 2, lambda x: x // 2)
    triple_value = (lambda x: x % 3, lambda x: x // 3)
    operations = (add, double_value, triple_value)
    min_num_operations = [np.inf] * (n+1)
    ways = [[] for _ in range((n + 1))]
    min_num_operations[0], min_num_operations[1] = 0, 1
    ways[1] = [1]
    for m in range(1, n+1):
        for operation in operations:
            if operation[0](m) == 0:
                num_operations = min_num_operations[operation[1](m)] + 1
                if num_operations < min_num_operations[m]:
                    min_num_operations[m] = num_operations
                    ways[m] = ways[operation[1](m)] + [m]
    return ways[n]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
