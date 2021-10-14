def words_to_sentence(words):
    return " ".join(words)


if __name__ == '__main__':
    assert words_to_sentence(['bacon', 'is', 'delicious']) == 'bacon is delicious'