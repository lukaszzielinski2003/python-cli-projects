class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Return the sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        Return the difference of a and b.
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Return the product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Return the quotient of a divided by b.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """
        Return a raised to the power of b.
        """
        return a**b
