from twttr import shorten

def test_str_without_vowels():
    for char in ['a', 'e', 'i', 'o', 'u']:
        assert shorten(char) == ''
    assert shorten("B") == 'B'
    assert shorten("Education") == 'dctn'
    assert shorten("1") == '1'
    assert shorten("Good Day!") == 'Gd Dy!'

def test_skip_all_upper_vowels():
    for char in ['A', 'E', 'I', 'O', 'U']:
        assert shorten(char) == ''
