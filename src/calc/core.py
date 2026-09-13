"""Core functions. Deliberately simple so the focus stays on the pipeline."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
