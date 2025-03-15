from calculator.utils import validate_number

def test_validate_number():
    # Valid numbers
    assert validate_number("42") is True
    assert validate_number("-15") is True
    assert validate_number("3.14") is True
    assert validate_number(".5") is True
    assert validate_number("123.456") is True

    # Invalid numbers
    assert validate_number("abc") is False
    assert validate_number("12a3") is False
    assert validate_number("") is False
    assert validate_number(" ") is False
    assert validate_number("1,000") is False
    assert validate_number("12.34.56") is False
