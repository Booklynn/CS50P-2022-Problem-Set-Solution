from um import count

def test_count():
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("um...") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1
    assert count("um, hello, um, world") == 2
    assert count("") == 0
    assert count(" ") == 0
    assert count("u m") == 0
    assert count("u.m") == 0
    assert count("!um") == 1
    assert count("um1") == 0
