def incrementer(nums):
    new_arr = []
    counter = 1
    for x in nums:
        x += counter
        counter += 1
        if x > 9:
            x = x % 10
        new_arr.append(x)
    return new_arr


if __name__ == '__main__':
    assert incrementer([]) == []
    assert incrementer([1, 2, 3]) == [2, 4, 6]
    assert incrementer([4, 6, 7, 1, 3]) == [5, 8, 0, 5, 8]
    assert incrementer([3, 6, 9, 8, 9]) == [4, 8, 2, 2, 4]
    assert incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]) == [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2]