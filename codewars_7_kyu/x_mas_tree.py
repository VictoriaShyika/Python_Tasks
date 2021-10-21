def xmastree(n):
    main_len = n * 2 - 1
    counter = n
    result = []
    x_counter = 1
    for i in range(1, n + 1):
        result.append('{1}{0}{1}'.format("#" * x_counter, "_" * int((main_len - x_counter) / 2)))
        counter -= 1
        x_counter += 2
    end_elem = '{1}{0}{1}'.format("#", "_" * int((main_len - 1) / 2))
    result.append(end_elem)
    result.append(end_elem)
    return result

if __name__ == '__main__':
    assert xmastree(3) == ['__#__', '_###_', '#####', '__#__', '__#__']
    assert xmastree(7) == ['______#______', '_____###_____', '____#####____', '___#######___', '__#########__', '_###########_', '#############', '______#______', '______#______']
    assert xmastree(2) == ['_#_', '###', '_#_', '_#_']
    assert xmastree(4) == ['___#___', '__###__', '_#####_', '#######', '___#___', '___#___']
    assert xmastree(6) == ['_____#_____', '____###____', '___#####___', '__#######__', '_#########_', '###########', '_____#_____', '_____#_____']