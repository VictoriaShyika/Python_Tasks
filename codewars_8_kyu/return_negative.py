def make_negative(number):
    return -abs(number)


if __name__ == '__main__':
    assert make_negative(42) == -42
    assert make_negative(-9) == -9
    assert make_negative(0) == 0