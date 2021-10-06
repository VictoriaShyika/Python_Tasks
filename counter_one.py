def ones_counter(inp):
    counter = 0
    result = []

    for i in inp:
        if i == 1:
            counter += 1
        else:
            if counter != 0:
                result.append(counter)
                counter = 0
    if counter != 0:
        result.append(counter)
    return result





if __name__ == '__main__':
    print(ones_counter([1, 1, 0, 1, 1, 1]))


