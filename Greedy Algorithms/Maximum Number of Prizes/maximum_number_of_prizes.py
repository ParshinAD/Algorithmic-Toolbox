# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    total = 0
    i = 0
    while total + i <n:
        i += 1
        summands.append(i)
        total += i
    summands[-1] += n-total

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)

