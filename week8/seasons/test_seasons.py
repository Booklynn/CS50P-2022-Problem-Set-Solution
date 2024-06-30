from seasons import convert
import pytest

def test_convert_min():
    assert convert("1999-01-01") == "Thirteen million, four hundred nine thousand, two hundred eighty minutes"

def test_convert_invalid():
    with pytest.raises(SystemExit, match="Invalid date"):
        convert("January 1, 1999")
