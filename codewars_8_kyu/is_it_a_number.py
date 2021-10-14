def isDigit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    assert isDigit("s2324") == False
    assert isDigit("-234.4") == True