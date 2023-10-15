from bank import value

def test_start_with_hello():
    assert value("Hello how are you?") == 0
    assert value("hElLo") == 0
    assert value("HELLO") == 0

def test_first_char_is_h():
    assert value("Hi?") == 20
    assert value("hi kekw?") == 20
    assert value("hI hOw are you?") == 20
    assert value("HI hOw are you?") == 20

def test_etc():
    assert value("What's up") == 100
    assert value("1") == 100
    assert value("!") == 100