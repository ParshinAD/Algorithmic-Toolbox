# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    new_m = from_index % 60
    new_n = from_index % 60 + (to_index - from_index) % 600

    if new_n in (0, 1):
        return new_n
    frst, scnd = 0, 1
    last_digit = 0
    flg = True

    for i in range(1, new_n+1):
        if flg:
            flg = False
        else:
            frst, scnd = scnd, (frst+scnd) % 10
        if i >= new_m:
            last_digit += scnd
            last_digit %= 10
    return last_digit


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
