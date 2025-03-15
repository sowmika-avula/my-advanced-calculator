def validate_number(value):
    """Validate if the input is a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False
