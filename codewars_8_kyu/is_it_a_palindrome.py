def is_palindrome(s):
    x = s.lower()
    y = s[::-1]
    if x == y.lower():
        x = True
    else:
        x = False
    return x


if __name__ == '__main__':
    assert is_palindrome('a') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('Abba') == True
    assert is_palindrome('malam') == True
    assert is_palindrome('walter') == False
    assert is_palindrome('kodok') == True
    assert is_palindrome('Kasue') == False