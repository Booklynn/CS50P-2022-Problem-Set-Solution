from numb3rs import validate

def test_correct_ip_address():
     assert validate("127.0.0.1") is True
     assert validate("255.255.255.255") is True
     assert validate("11.99.22.88") is True
     assert validate("1.2.3.4") is True

def test_incorrect_ip_address():
     assert validate("cat") is False
     assert validate("1.2.3.1000") is False
     assert validate("512.512.512.512") is False
     assert validate("275.3.6.28") is False
     assert validate("199.911.288.882") is False