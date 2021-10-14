def vaporcode(s):
    s = s.replace(" ", "")
    return "  ".join(s.upper())


if __name__ == '__main__':
    assert vaporcode("Lets go to the movies") == "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
    assert vaporcode("Why isn't my code working?") == "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"