from plates import is_valid

def test_plates_len_less_than_2():
    assert is_valid("") == False
    assert is_valid("1") == False
    assert is_valid("a") == False

def test_plates_len_more_than_6():
    assert is_valid("AAA2222") == False

def test_plates_start_with_2_letters():
    assert is_valid("a1") == False
    assert is_valid("1A") == False

def test_plates_start_with_0():
    assert is_valid("0AA222") == False

def test_plates_number_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_plates_punctuation():
    assert is_valid("CS50!") == False

def test_valid():
    assert is_valid("AAA222") == True
    assert is_valid("cs50") == True
    assert is_valid("HELLO") == True