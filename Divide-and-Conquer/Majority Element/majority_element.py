# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    def rec(elements):
        if len(elements) == 1:
            return elements[0]
        first_half = rec(elements[:len(elements) // 2])
        second_half = rec(elements[len(elements) // 2:])

        if first_half == second_half:
            return first_half

        first_count = elements.count(first_half)
        second_count = elements.count(second_half)
        if first_count > second_count:
            return first_half
        else:
            return second_half

    if elements.count(rec(elements)) > len(elements) / 2:
        return 1
    return 0



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
