# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    return (money // 10) + ((money % 10) // 5) + ((money % 10) % 5)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
