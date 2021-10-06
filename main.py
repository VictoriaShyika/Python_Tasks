def last_survivor(letters, coords):
    letters_list = list(letters)
    for num in coords:
        strdel(letters_list[num])
    return letters


if __name__ == '__main__':
    print(last_survivor('abc', [1, 1]))

