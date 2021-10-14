def hex_to_dec(s):
    answer = 0
    counter = 1
    for char in reversed(s):
        if char == "f":
            answer += 15 * counter
        elif char == "e":
            answer += 14 * counter
        elif char == "d":
            answer += 13 * counter
        elif char == "c":
            answer += 12 * counter
        elif char == "b":
            answer += 11 * counter
        elif char == "a":
            answer += 10 * counter
        else:
            answer += int(char) * counter
        counter *= 16
    return answer


if __name__ == '__main__':
    assert hex_to_dec("1") == 1
    assert hex_to_dec("a") == 10
    assert hex_to_dec("10") == 16