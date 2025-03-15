import operator

class Calculator:
    def __init__(self):
        self.operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

    def evaluate_expression(self, expression: str) -> float:
        """Evaluate a simple arithmetic expression."""
        try:
            parts = expression.split()
            if len(parts) != 3:
                raise ValueError("Expression must have exactly 3 parts (e.g., '2 + 3')")
            left, operator_symbol, right = parts
            if operator_symbol not in self.operations:
                raise ValueError(f"Unsupported operator: {operator_symbol}")
            return self.operations[operator_symbol](float(left), float(right))
        except (ValueError, ZeroDivisionError) as error:
            raise error

    @staticmethod
    def add(first_number: float, second_number: float) -> float:
        return first_number + second_number

    @staticmethod
    def subtract(first_number: float, second_number: float) -> float:
        return first_number - second_number

    @staticmethod
    def multiply(first_number: float, second_number: float) -> float:
        return first_number * second_number

    @staticmethod
    def divide(first_number: float, second_number: float) -> float:
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number

    def divide_lbyl(self, first_number: float, second_number: float) -> float:
        """Divide using Look Before You Leap (LBYL)."""
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number

    def divide_eafp(self, first_number: float, second_number: float) -> float:
        """Divide using Easier to Ask for Forgiveness than Permission (EAFP)."""
        try:
            return first_number / second_number
        except ZeroDivisionError as error:
            raise ZeroDivisionError("Cannot divide by zero.") from error
