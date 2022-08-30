# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    max_index = -1
    for i in range(len(numbers)):
        if max_index == -1 or numbers[max_index] < numbers[i]:
            max_index = i
    max_index2 = -1
    for i in range(len(numbers)):
        if max_index != i and (max_index2 == -1 or numbers[max_index2] < numbers[i]):
            max_index2 = i
    return numbers[max_index] * numbers[max_index2]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
