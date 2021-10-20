def minimum_steps(numbers, value):
    result = 0
    counter = 0
    for i in sorted(numbers):
        result += i
        if result < value:
            counter += 1
    return counter

if __name__ == '__main__':
    assert minimum_steps([4, 6, 3], 7) == 1
    assert minimum_steps([10, 9, 9, 8], 17) == 1
    assert minimum_steps([8, 9, 10, 4, 2], 23) == 3
    assert minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464) == 8
    assert minimum_steps([4, 6, 3], 2) == 0