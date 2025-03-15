from calculator.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2

def test_divide_by_zero():
    calc = Calculator()
    try:
        calc.divide(5, 0)
    except ZeroDivisionError:
        assert True

def test_evaluate_expression_valid():
    calc = Calculator()
    assert calc.evaluate_expression("2 + 3") == 5

def test_evaluate_expression_invalid_format():
    calc = Calculator()
    try:
        calc.evaluate_expression("2 +")
    except ValueError as e:
        assert str(e) == "Expression must have exactly 3 parts (e.g., '2 + 3')"

def test_evaluate_expression_unsupported_operator():
    calc = Calculator()
    try:
        calc.evaluate_expression("2 ^ 3")
    except ValueError as e:
        assert str(e) == "Unsupported operator: ^"

def test_evaluate_expression_invalid_expression():
    calc = Calculator()
    try:
        calc.evaluate_expression("invalid")
    except ValueError as e:
        assert "Expression must have exactly 3 parts (e.g., '2 + 3')" in str(e)

def test_divide_lbyl():
    calc = Calculator()
    assert calc.divide_lbyl(6, 3) == 2
    try:
        calc.divide_lbyl(5, 0)
    except ZeroDivisionError:
        assert True

def test_divide_eafp():
    calc = Calculator()
    assert calc.divide_eafp(6, 3) == 2
    try:
        calc.divide_eafp(5, 0)
    except ZeroDivisionError:
        assert True
