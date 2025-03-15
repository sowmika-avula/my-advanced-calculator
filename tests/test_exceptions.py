from calculator.exceptions import CalculatorError, DivisionByZeroError

def test_calculator_error():
    try:
        raise CalculatorError("Test error")
    except CalculatorError as e:
        assert str(e) == "Test error"

def test_division_by_zero_error():
    try:
        raise DivisionByZeroError()
    except DivisionByZeroError as e:
        assert str(e) == "Cannot divide by zero"
