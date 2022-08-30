# python3
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    def rec(low, hight):
        if hight <= low:
            return -1
        median = int(low + (hight - low) / 2)
        if keys[median] == query:
            return median
        elif keys[median] > query:
            return rec(low, median)
        else:
            return rec(median + 1, hight)

    return rec(0, len(keys))



if __name__ == '__main__':
    input()
    input_keys = list(map(int, input().split()))
    input()
    input_queries = list(map(int, input().split()))

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
