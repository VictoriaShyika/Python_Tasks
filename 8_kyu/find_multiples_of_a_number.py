def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))


if __name__ == '__main__':
    assert find_multiples(5, 25) == [5, 10, 15, 20, 25]
    assert find_multiples(1, 2) == [1, 2]