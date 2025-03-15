class CalculatorError(Exception):
    """Base exception for calculator-related errors."""

    def __init__(self, message="Calculator error"):
        super().__init__(message)


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    def __init__(self, message="Cannot divide by zero"):
        super().__init__(message)
