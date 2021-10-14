def high_and_low(numbers):
    new_list = list(map(int, numbers.split()))
    return '{} {}'.format(max(new_list), min(new_list))


if __name__ == '__main__':
    assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
    assert high_and_low("1 2 3") == "3 1"
