def bin_to_decimal(inp):
    answer = 0
    counter = 1
    for x in reversed(inp):
        answer += int(x) * counter
        counter *= 2
    return answer
if __name__ == '__main__':
    assert bin_to_decimal("0") == 0
    assert bin_to_decimal("1") == 1
    assert bin_to_decimal("10") == 2
    assert bin_to_decimal("11") == 3
    assert bin_to_decimal("101010") == 42
    assert bin_to_decimal("1001001") == 73