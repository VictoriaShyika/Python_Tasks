def two_sort(array):
    return "***".join(sorted(array)[0])


if __name__ == '__main__':
    assert two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]) == 'b***i***t***c***o***i***n'
    assert two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]) == 'a***r***e'
    assert two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]) == 'a***b***o***u***t'
    assert two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]) == 'c***o***d***e'
    assert two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]) == 'L***e***t***s'