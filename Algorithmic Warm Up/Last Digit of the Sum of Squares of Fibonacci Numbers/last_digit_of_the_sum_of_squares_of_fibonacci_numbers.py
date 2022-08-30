# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    new_n = n % 60
    if not new_n:
        return 0, 0
    frst, scnd = 0, 1
    last_digit = 1
    for i in range(1, new_n):
        frst, scnd = scnd, (frst+scnd)%10
    return frst, scnd


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    first, second = last_digit_of_the_fibonacci_numbers(n)
    return (second * (first+second))%10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
