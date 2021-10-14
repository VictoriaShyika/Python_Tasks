def to_alternating_case(string):
    return string.swapcase()


if __name__ == '__main__':
    assert to_alternating_case("hello world") =="HELLO WORLD"
    assert to_alternating_case("HELLO WORLD") =="hello world"
    assert to_alternating_case("hello WORLD") =="HELLO world"
    assert to_alternating_case("HeLLo WoRLD") =="hEllO wOrld"
    assert to_alternating_case("12345") =="12345"
    assert to_alternating_case("1a2b3c4d5e") =="1A2B3C4D5E"
    assert to_alternating_case("String.prototype.toAlternatingCase") =="sTRING.PROTOTYPE.TOaLTERNATINGcASE"