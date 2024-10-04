def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return "The result of the division is "+result
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero."
    except ValueError:
        result = "Error: Please enter numeric values only."